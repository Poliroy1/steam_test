from selenium.common import WebDriverException

from logger.logger import Logger
from elements.input import Input
from selenium.webdriver.common.keys import Keys


class SliderElement(Input):
    def get_min_value(self) -> float:
        return float(self.get_attribute("min"))

    def get_max_value(self) -> float:
        return float(self.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.get_attribute("step"))

    def get_current_value(self) -> float:
        return float(self.get_attribute("value"))

    def _send_keys(self, keys: str):
        element = self.wait_for_visible()
        Logger.info(f"{self}: send keys = '{repr(keys)}'")
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def set_value(self, target_value: float):
        Logger.info(f"Setting slider to value {target_value}")

        min_value = self.get_min_value()
        max_value = self.get_max_value()
        step = self.get_step()
        current_value = self.get_current_value()

        if not min_value < target_value < max_value:
            raise ValueError("Target value must be inside slider range")

        steps = int((target_value - current_value) / step)
        if steps == 0:
            return
        key = Keys.ARROW_RIGHT if steps > 0 else Keys.ARROW_LEFT

        self.click()
        self._send_keys(Keys.HOME)
        self._send_keys(key * steps)
