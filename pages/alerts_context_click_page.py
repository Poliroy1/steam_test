from browser.browser import Browser
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class AlertsContextClickPage(BasePage):
    UNIQUE_ELEMENT_LOC = "hot-spot"
    HOT_SPOT = "hot-spot"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Context click'
        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description="Unique element -> Label")
        self.hot_spot_window = WebElement(self.browser, self.HOT_SPOT, description="Context click -> WebElement")

    def click_right_button(self) -> None:
        Logger.info(f"{self}: click right button")
        action_chains = ActionChains(self.browser.driver)
        element = self.hot_spot_window.wait_for_clickable()
        action_chains.context_click(element).perform()
