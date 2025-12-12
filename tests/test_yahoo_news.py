from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from pathlib import Path
import pytest
import json
import os

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
    # Instantiate the tab and get the bottom navigation bar
    elements = driver.find_elements(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.yahoo.mobile.client.android.yahoo:id/bottomTabBar']//android.widget.TextView")
    expected_values = ['Home', 'Top stories', 'Notifications', 'Profile']
    for idx, element in enumerate(elements):
        assert expected_values[idx] == element.text
    assert True