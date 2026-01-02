from core.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(),'Hovers')]"
    AVATARS = "(//*[contains(@src,'avatar')])[{}]"
    USER_NAME = "//*[contains(text(),'name: user{}')]"
    PROFILE_LINK = "//*[contains(text(),'users/{}')]"


    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.page_name = "Hovers Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description="Unique element -> WebElement")
        self.avatars = MultiWebElement(self.browser, self.AVATARS, description="User avatars")

    def hover_avatar(self, avatar: WebElement) -> None:
        """Наведение на аватар с проверкой существования"""
        if avatar.is_exists():
            Logger.info(f"{self}: hover avatar")
            avatar.hover  # без скобок, потому что hover — property
        else:
            Logger.error(f"{self}: Avatar не найден")

    def get_user_name(self, index: int) -> str:
        return WebElement(
            self.browser,
            self.USER_NAME.format(index),
            f"User name user{index}"
        ).get_text()

    def click_profile_link(self, index: int) -> None:
        WebElement(
            self.browser,
            self.PROFILE_LINK.format(index),
            f"Profile link user{index}"
        ).click()

    def hover_and_get_user_name(self, index: int) -> str:
        """Наводим на аватар и ждём появления имени пользователя"""
        avatar = self.avatars.get_element(index)
        self.hover_avatar(avatar)  # использует проверку is_exists()
        return self.get_user_name(index)