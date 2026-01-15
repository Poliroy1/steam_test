from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(),'Hovers')]"
    AVATARS = "(//*[contains(@class,'figure')])[{}]"
    USER_NAME = "(//*[contains(text(),'name: user')])[{}]"
    PROFILE_LINK = "(//*[contains(@href,'/users/')])[{}]"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.page_name = "Hovers Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Unique element -> WebElement")
        self.avatars = MultiWebElement(self.browser, self.AVATARS, description="User avatars")

    def hover_avatar(self, avatar: WebElement) -> None:
        if avatar.is_exists():
            Logger.info(f"{self}: hover avatar")
            avatar.hover()
        else:
            raise ValueError(f"{self}: Avatar не найден")

    def _get_user_name(self, index: int) -> str:
        return WebElement(
            self.browser,
            self.USER_NAME.format(index + 1),
            f"User name user{index}"
        ).get_text()

    def _click_profile_link(self, index: int) -> None:
        WebElement(
            self.browser,
            self.PROFILE_LINK.format(index + 1),
            f"Profile link user{index}"
        ).wait_for_clickable().click()

    def hover_and_click_profile(self, index: int) -> str:
        Logger.info(f"{self}: trying to find all users")
        avatars = self.avatars.get_all_elements()
        avatar = avatars[index]
        self.hover_avatar(avatar)
        user_name = self._get_user_name(index)
        self._click_profile_link(index)
        return user_name
