from core.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class AlertsContextClick(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='hot-spot']"
    HOT_SPOT = "//*[@id='hot-spot']"


    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Context click'
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description="Unique element -> WebElement")
        self.hot_spot_window = WebElement(self.browser, self.HOT_SPOT, description="Context click -> WebElement")

    def click_right_button(self) -> None:
        Logger.info(f"{self}: click right button")
        action_chains = ActionChains(self.browser.driver)
        element = self.hot_spot_window.wait_for_presence()
        action_chains.context_click(element).perform()

    def get_alert_text(self) -> None:
        Logger.info(f"{self}: get alert text")
        text = self.browser.get_alert_text()
        return text

    def accept_alert(self) -> None:
        Logger.info(f"{self}: accept alert")
        self.browser.accept_alert()





