from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path
import pytest
import json
import os
from src.constants.enums import Platform, DeviceProvider
from src.pages.notes.notes import NotesPage
from src.pages.yahoo_news.home import HomePage

# Keep as global variables for the test.  These should be set in the conftest or config for production
PLATFORM = Platform(os.environ.get("PLATFORM", Platform.ANDROID.value))
PROVIDER = DeviceProvider(os.environ.get("PROVIDER", DeviceProvider.LOCAL.value))


@pytest.fixture(scope="function")
def capabilities(request):
    """
    Fixture to load the capabilities for the app session.
    Keeping within the test file.  Production code would live elsewhere such as conftest.py
    """
    app_name = request.param
    app_config = (
        Path(__file__).parent.parent
        / "config"
        / f"{PLATFORM.value}"
        / f"{app_name}.json"
    )
    if not os.path.exists(app_config):
        Exception(
            f"The config for app {app_name} does not exist on platform {PLATFORM.value}"
        )
    with open(app_config, "r") as f:
        capabilities = json.load(f)
    yield capabilities


@pytest.fixture(scope="function")
def driver(capabilities):
    """
    Fixture to generate the driver to interact with the mobile applications.
    Keeping the driver within the test for assessment purpose.
    Production code involes placing the driver into a DriverFactory
    """
    options = None
    # Construct options based on the platform
    if PLATFORM == Platform.ANDROID:
        options = UiAutomator2Options().load_capabilities(capabilities)
    if PLATFORM == Platform.IOS:
        Exception(f"Not implemented for platform {Platform.IOS.value}")

    # Determine the host: default to local as cloud could vary e.g. Browserstack Saucelabs, etc.
    host = None
    if PROVIDER == DeviceProvider.LOCAL:
        host = "http://localhost:4723"

    driver = webdriver.Remote(
        host,
        options=options,
    )
    yield driver
    driver.terminate_app(capabilities["appium:appPackage"])
    driver.quit()


@pytest.fixture
def notes_app():
    if PLATFORM == Platform.ANDROID:
        return "com.google.android.keep"


@pytest.mark.parametrize("capabilities", ["yahoo_news"], indirect=True)
def test_yahoo_news_get_bottom_tab(driver, notes_app):
    # ARRANGE
    yahoo_news_page = HomePage(driver, PLATFORM)

    # ACT
    # Verify that the bottom nav elements are retrieved
    bottom_nav_elements = yahoo_news_page.bottom_tab()

    # ASSERT
    # Verify that the bottom nav text matches the expected values
    expected_values = ["Home", "Top stories", "Notifications", "Profile"]
    for idx, element in enumerate(bottom_nav_elements):
        assert expected_values[idx] == element.text

    # Construct the value to be added onto the notes
    content = ",".join(element.text for element in bottom_nav_elements)
    written_content = None

    # Start the Notes app for the platform
    try:
        driver.activate_app(notes_app)
        notes_page = NotesPage(driver, PLATFORM)
        # Keep the android specific steps for when test has to support android + ios
        if PLATFORM == PLATFORM.ANDROID:
            notes_page.note_options_button().click()
            notes_page.start_note_button().click()
            notes_page.notes_text_field().send_keys(content)

        # Capture the value and compare it to the content
        written_content = notes_page.notes_text_field().text

        # TODO: Add proper teardown to delete the notes artifact
    except:
        print("Failed to interact with notes app.")
    finally:
        driver.terminate_app(notes_app)

    assert written_content == content
