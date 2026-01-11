from bs4 import BeautifulSoup

from elements.label import Label
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//h3[contains(text(), 'Infinite Scroll')]"
    PARAGRAPHS = "(//*[contains(@class, 'jscroll-added')])"
    LOC_ALL_PARAGRAPH = "//div[contains(@class, 'jscroll-inner')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'Infinity scroll page'

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.paragraphs = MultiWebElement(self.browser, self.PARAGRAPHS, description='Text Paragraph -> MultiWebElement')
        self.all_paragraph_elem = WebElement(self.browser, self.LOC_ALL_PARAGRAPH,description='Paragraphs elem -> WebElement')

    def get_paragraph(self, my_age):
        while True:
            self.all_paragraph_elem.scroll_to_element()
            soup = BeautifulSoup(self.all_paragraph_elem.get_attribute('innerHTML'), 'html.parser')
            rows = soup.find_all(class_='jscroll-added')
            if len(rows) == my_age:
                return rows