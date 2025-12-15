from appium.webdriver.common.appiumby import AppiumBy
from src.constants.enums import Platform
from src.pages.base import BasePage


class HomePage(BasePage):
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform

    def bottom_tab(self):
        if self.platform == Platform.ANDROID:
            return self.find_all(
                (
                    AppiumBy.XPATH,
                    "//androidx.compose.ui.platform.ComposeView[@resource-id='com.yahoo.mobile.client.android.yahoo:id/bottomTabBar']//android.widget.TextView",
                )
            )

        if self.platform == Platform.IOS:
            pass
