from elements.web_element import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from logger.logger import Logger
from selenium.webdriver.common.keys import Keys


class SliderElement(WebElement):
    def __init__(self, browser, locator, description="Slider"):
        super().__init__(browser, locator, description)

    def get_min_value(self) -> float:
        return float(self.get_attribute("min"))

    def get_max_value(self) -> float:
        return float(self.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.get_attribute("step"))

    def set_value(self, target_value: float, current_value: float) -> None:
        Logger.info(f"Setting slider to value {target_value}")

        min_value = self.get_min_value()
        max_value = self.get_max_value()
        step = self.get_step()

        if not min_value < target_value < max_value:
            raise ValueError("Target value must be inside slider range")

        steps = int(round((target_value - current_value) / step))
        key = Keys.ARROW_RIGHT if steps > 0 else Keys.ARROW_LEFT

        slider_element = self.get_element
        action = ActionChains(self.browser.driver).click(slider_element)
        for _ in range(abs(steps)):
            action.send_keys(key)
        action.perform()