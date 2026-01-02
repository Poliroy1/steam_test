
from core.browser import Browser
from elements.label import Label
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage


class DynamicPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Dynamic Content')]"
    IMAGES = "//*[@id='content']//img"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Dynamic content page'

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.images = MultiWebElement(self.browser, self.IMAGES, description='Content images -> Label')

    def get_image_src(self) -> list[str]:
        return [img.get_attribute("src") for img in self.images]


    def get_duplicate_image_src(self) -> list[str]:
        Logger.info(f"{self}: get_duplicate_image_src")
        while True:
            images_list = self.get_image_src()

            if len(images_list) > len(set(images_list)):
                Logger.info(f"{self}: Дубликаты найдены!")
                return images_list
            else:
                Logger.info(f"{self}: Дубликатов пока нет, перезагрузка...")
                self.browser.refresh()