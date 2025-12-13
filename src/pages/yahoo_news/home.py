from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base import BasePage


class HomePage(BasePage):
    def __init__(self, driver, platform: str):
        self.driver = driver
        self.platform = platform

    def bottom_tab(self):
        if self.platform == "android":
            return self.find_all(
                (
                    AppiumBy.XPATH,
                    "//androidx.compose.ui.platform.ComposeView[@resource-id='com.yahoo.mobile.client.android.yahoo:id/bottomTabBar']//android.widget.TextView",
                )
            )

        if self.platform == "ios":
            pass
