from elements.label import Label
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = ''
    PARAGRAPHS = "(//div[@class='jscroll-added'])[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'Infinity scroll page'

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.paragraphs = MultiWebElement(self.browser, self.PARAGRAPHS, description='Text Paragraph -> MultiWebElement')

    def get_paragraph_count(self) -> int:
        Logger.info(f'{self} Получаем текущее кол-во параграфов')
        return len(self.paragraphs)

    def scroll_until_paragraph_count(self, expected_count: int):
        Logger.info(f"{self} Скроллим до expected_count")
        current_count = self.get_paragraph_count()
        attempt = 1
        while current_count < expected_count:
            Logger.info(f"{self}: Прокрутка вниз, попытка {attempt}, текущие абзацы: {current_count}")
            self.browser.driver.execute_script("window.scrollBy(0, 500);")  # скролл вниз на 500 пикселей
            current_count = self.get_paragraph_count()
            attempt += 1

