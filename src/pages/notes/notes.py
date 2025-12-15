from appium.webdriver.common.appiumby import AppiumBy
from src.constants.enums import Platform
from src.pages.base import BasePage


class NotesPage(BasePage):
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform

    def note_options_button(self):
        if self.platform == Platform.ANDROID:
            return self.find(
                (
                    AppiumBy.ID,
                    "com.google.android.keep:id/speed_dial_create_close_button",
                )
            )

        if self.platform == Platform.IOS:
            pass

    def start_note_button(self):
        if self.platform == Platform.ANDROID:
            return self.find(
                (AppiumBy.ID, "com.google.android.keep:id/new_note_button")
            )

        if self.platform == Platform.IOS:
            pass

    def notes_text_field(self):
        if self.platform == Platform.ANDROID:
            return self.find((AppiumBy.ID, "com.google.android.keep:id/edit_note_text"))

        if self.platform == Platform.IOS:
            pass
