from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base import BasePage


class NotesPage(BasePage):
    def __init__(self, driver, platform: str):
        self.driver = driver
        self.platform = platform

    def note_options_button(self):
        if self.platform == "android":
            return self.find(
                (
                    AppiumBy.ID,
                    "com.google.android.keep:id/speed_dial_create_close_button",
                )
            )

        if self.platform == "ios":
            pass

    def start_note_button(self):
        if self.platform == "android":
            return self.find(
                (AppiumBy.ID, "com.google.android.keep:id/new_note_button")
            )

        if self.platform == "ios":
            pass

    def notes_text_field(self):
        if self.platform == "android":
            return self.find((AppiumBy.ID, "com.google.android.keep:id/edit_note_text"))

        if self.platform == "ios":
            pass
