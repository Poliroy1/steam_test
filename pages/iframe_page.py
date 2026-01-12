from browser.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from elements.label import Label
from elements.button import Button

class IframePage(BasePage):

    UNIQUE_ELEMENT_LOC = "//*[@id='app']//*[contains(@class,'text-center')]"
    ALERTS_MENU = "//*[@id='app']//*[contains(@class, 'header-text') and contains (., 'Alerts, Frame & Windows')]"
    NESTED_FRAMES_BUTTON = "//*[@id='app']//*[contains(@class, 'text') and contains(text(), 'Nested Frames')]"
    CHILD_IFRAME = "//iframe"
    PARENT_FRAME = "//*[@id='frame1']"
    PARENT_TEXT = "//*[contains(text(), 'Parent frame')]"
    CHILD_TEXT = "//*[contains(text(), 'Child Iframe')]"
    FRAMES_BUTTON = "//*[@id='item-2']//*[contains(@class, 'text') and contains(text(), 'Frames')]"
    UP_FRAME = "//*[@id='frame1']"
    DOWN_FRAME = "//*[@id='frame2']"
    HEADER = "//*[@id='sampleHeading']"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.page_name = 'iframe'

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC, description='Unique element -> Label')
        self.alerts_menu = Button(self.browser, self.ALERTS_MENU, description='Alerts menu button')
        self.nested_element = Button(self.browser, self.NESTED_FRAMES_BUTTON, description='Nested element -> Button')
        self.child_iframe = WebElement(self.browser, self.CHILD_IFRAME, description='IFRAME One -> WebElement')
        self.parent_frame = WebElement(self.browser, self.PARENT_FRAME, description='IFRAME Two -> WebElement')
        self.parent_text = WebElement(self.browser, self.PARENT_TEXT, description='Parent text -> WebElement')
        self.child_text = WebElement(self.browser, self.CHILD_TEXT, description='Child text -> WebElement')
        self.frames_button = Button(self.browser, self.FRAMES_BUTTON, description='Click Button -> Button')
        self.up_frame = WebElement(self.browser, self.UP_FRAME, description='UP Frame -> WebElement')
        self.down_frame = WebElement(self.browser, self.DOWN_FRAME, description='DOWN Frame -> WebElement')
        self.header = WebElement(browser, self.HEADER, description="Header -> WebElement")

    def click_alerts_menu(self):
        Logger.info(f"{self} Click alerts menu button")
        self.alerts_menu.js_click()

    def click_nested(self):
        Logger.info(f"{self} Click Nested Frame")
        self.nested_element.js_click()

    def get_child_text(self) -> str:
        self.browser.switch_to_frame(self.parent_frame)
        self.browser.switch_to_frame(self.child_iframe)
        text = self.child_text.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_parent_text(self) -> str:
        self.browser.switch_to_frame(self.parent_frame)
        text = self.parent_text.get_text()
        self.browser.switch_to_default_content()
        return text

    def click_frames(self) -> None:
        Logger.info(f"{self} Click Frames")
        self.frames_button.js_click()

    def get_text_to_up_iframe(self) -> str:
        Logger.info(f"{self} Click Up Frame")
        self.browser.switch_to_frame(self.up_frame)
        text = self.header.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_text_to_down_iframe(self) -> str:
        Logger.info(f"{self} Click Down Frame")
        self.browser.switch_to_frame(self.down_frame)
        text = self.header.get_text()
        self.browser.switch_to_default_content()
        return text


