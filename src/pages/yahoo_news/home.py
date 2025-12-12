from appium.webdriver.common.appiumby import AppiumBy

class HomePage:

    def __init__(self, driver, platform: str):
        self.driver = driver
        self.platform = platform
    
    def bottom_tab(self):
        if self.platform == 'android':
            return self.driver.find_elements(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.yahoo.mobile.client.android.yahoo:id/bottomTabBar']//android.widget.TextView")

        if self.platform == 'ios':
            pass