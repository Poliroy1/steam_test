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
        self.correct_value = WebElement(self.browser, self.CORRECT_VALUE, description="Correct value -> WebElement")

    def get_correct_value(self) -> float:
        Logger.info(f"{self}, Getting correct value")
        return float(self.correct_value.get_text())

    def set_random_slider_value(self, possible_values: list[float] | None = None) -> float:

        if possible_values is None:
            min_value = self.slider.get_min_value()
            max_value = self.slider.get_max_value()
            step = self.slider.get_step()

            possible_values = [
                min_value + i * step
                for i in range(1, int((max_value - min_value) / step))
            ]

        target_value = random.choice(possible_values)
        Logger.info(f"{self}, Random target value: {target_value}")

        self.slider.set_value(target_value)

        return target_value
