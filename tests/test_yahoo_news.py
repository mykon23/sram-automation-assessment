from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path
import pytest
import json
import os
from src.pages.yahoo_news.home import HomePage

@pytest.fixture(scope='function')
def capabilities(request) -> dict:
    app_name = request.param
    platform = os.environ.get('PLATFORM', 'android')
    app_config = Path(__file__).parent.parent / 'config' / f'{platform}' / f'{app_name}.json'
    if not os.path.exists(app_config):
        Exception(f"The config for app {app_name} does not exist on platform {platform}")
    with open(app_config, 'r') as f:
        capabilities = json.load(f)
    yield capabilities

@pytest.fixture(scope='function')
def driver(capabilities):
    driver = webdriver.Remote('http://localhost:4723',
                          options=UiAutomator2Options().load_capabilities(capabilities)
                          )
    yield driver
    driver.terminate_app(capabilities['appium:appPackage'])
    driver.quit()

@pytest.mark.parametrize("capabilities", ["yahoo_news"], indirect=True)
def test_yahoo_news_get_bottom_tab(driver):
    # ARRANGE
    yahoo_news_page = HomePage(driver, os.environ.get('PLATFORM', 'android'))

    # ACT
    # Verify that the bottom nav elements are retrieved
    bottom_nav_elements = yahoo_news_page.bottom_tab()

    # ASSERT
    # Verify that the bottom nav text matches the expected values
    expected_values = ['Home', 'Top stories', 'Notifications', 'Profile']
    for idx, element in enumerate(bottom_nav_elements):
        assert expected_values[idx] == element.text
    assert True