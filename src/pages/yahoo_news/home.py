from appium.webdriver.common.appiumby import AppiumBy
import os

class HomePage:

    def __init__(self, driver, platform: str):
        self.driver = driver
        self.platform = platform
    
    def bottom_tab(self):
        elements = None
        if self.platform == 'android':
            elements = self.driver.find_elements(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.yahoo.mobile.client.android.yahoo:id/bottomTabBar']//android.widget.TextView")
            return elements

        if self.platform == 'ios':
            pass