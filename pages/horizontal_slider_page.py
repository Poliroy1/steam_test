import random

from browser.browser import Browser
from elements.web_element import WebElement
from elements.slider import SliderElement
from logger.logger import Logger
from pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "range"
    SLIDER = "//*[@id='content']//*[@type='range']"
    CORRECT_VALUE = "range"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.page_name = 'Slider Page'
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="Unique element -> WebElement")
        self.slider = SliderElement(self.browser, self.SLIDER, description="Horizontal slider -> WebElement")
        self.current_value = WebElement(self.browser, self.CORRECT_VALUE, description="Correct value -> WebElement")

    def get_current_value(self) -> float:
        Logger.info(f"{self}, Getting correct value")
        return float(self.current_value.get_text())

    def get_slider_bounds(self) -> tuple[float, float, float]:
        return (
            self.slider.get_min_value(),
            self.slider.get_max_value(),
            self.slider.get_step(),
        )

    def set_slider_value(self, value: float):
        Logger.info(f"{self}: Setting slider to value {value}")
        return self.slider.set_value(value)
