from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class DynamicPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Dynamic Content')]"
    IMAGES = "(//*[@id='content']//img)[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Dynamic content page'

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.images = MultiWebElement(self.browser, self.IMAGES, description='Content images -> Label')

    def get_duplicate_image_src(self, count_refresh):
        Logger.info(f"{self}: get_duplicate_image_src")
        count = 0
        while count < count_refresh:
            images_list = [img.get_attribute("src") for img in self.images]

            if len(images_list) > len(set(images_list)):
                Logger.info(f"{self}: Дубликаты найдены!")
                return images_list

            Logger.info(f"{self}: Дубликатов пока нет, перезагрузка...")
            self.browser.refresh()
            count += 1

        raise AssertionError (f"{count} кол-во повторений не совпало")