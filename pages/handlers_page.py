from core.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Opening a new window')]"
    LINK = "//*[@id='content']//*[@target='_blank'])]"
    HEADER = "//*[@class='example']//*[contains(text(), 'New window')]"


    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.page_name = ''

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description="Unique element -> WebElement")
        self.link = WebElement(self.browser, self.LINK, description="Link -> WebElement")
        self.header = WebElement(self.browser, self.HEADER, description="Header -> WebElement")

    def click_link(self) -> None:
        Logger.info(f"{self.page_name} click link")
        self.link.click()

    def get_title(self) -> None:
        Logger.info(f"{self.page_name} get title")
        title = self.browser.driver.title
        return title

    def get_header_text(self) -> None:
        Logger.info(f"{self.page_name} get header text")
        return self.header.get_text()




