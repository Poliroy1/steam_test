from browser.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger
from .base_page import BasePage

class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Basic Auth')]"
    SUCCESS_TEXT_LOC = "//*[@id='content']//*[contains(text(), 'Congratulations!')]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Basic Auth"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description='Basic Auth page title -> Open Page')
        self.success_text_element = WebElement(self.browser, self.SUCCESS_TEXT_LOC, description='Success message text -> Get Text')

    def is_logged_in(self):
        Logger.info(f"{self} is_logged_in")
        return self.success_text_element.get_text()

