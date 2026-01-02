from faker import Faker

from core.browser import Browser
from elements.web_element import WebElement
from elements.button import Button

from logger.logger import Logger
from pages.base_page import BasePage

faker = Faker()

class AlertsJSPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='page-footer']"

    JS_ALERT_BUTTON = "//button[@onclick='jsAlert()']"
    JS_CONFIRM_BUTTON = "//button[@onclick='jsConfirm()']"
    JS_PROMPT_BUTTON = "//button[@onclick='jsPrompt()']"
    RESULT_TEXT = "//*[@id='result']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "JavaScript Alerts"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description='JS Alert -> WebElement')
        self.js_alert_button = Button(self.browser, self.JS_ALERT_BUTTON, description='JS Alert button -> Submit Button')
        self.text_results = WebElement(self.browser, self.RESULT_TEXT, description='JS Alert -> Text Results')
        self.js_confirm_button = Button(self.browser, self.JS_CONFIRM_BUTTON, description='JS Confirm button -> Submit Button')
        self.js_prompt_button = Button(self.browser, self.JS_PROMPT_BUTTON, description='JS Prompt button -> Submit Button')

    def js_click_js_alert(self) -> None:
        Logger.info(f"{self.page_name}: click JS Alert button")
        self.js_alert_button.js_click()

    def js_click_js_confirm(self) -> None:
        Logger.info(f"{self.page_name}: click JS Confirm button")
        self.js_confirm_button.js_click()

    def js_click_js_prompt(self) -> None:
        Logger.info(f"{self.page_name}: click JS Prompt button")
        self.js_prompt_button.js_click()

    def get_alert_text(self) -> None:
        Logger.info(f"{self}: get alert text")
        text = self.browser.get_alert_text()
        return text

    def accept_alert(self) -> None:
        Logger.info(f"{self}: accept alert")
        self.browser.accept_alert()







