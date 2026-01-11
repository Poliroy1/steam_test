from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from browser.browser import Browser
from logger.logger import Logger


class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            browser: "Browser",
            locator: str | tuple,
            description: str = None,
            timeout: int = DEFAULT_TIMEOUT,
    ):
        self.browser = browser
        self.timeout = timeout

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

        self.description = description if description else str(locator)

        self._wait = WebDriverWait(browser.driver, timeout)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.description})"

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self}: wait for {expected_condition.__name__}")
            element = self._wait.until(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}:{err}")
            raise

    def _wait_for_not(self, expected_condition) -> None:
        try:
            Logger.info(f"{self}: wait for not {expected_condition.__name__}")
            self._wait.until(method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}:{err}")
            raise

    def wait_for_presence(self) -> WebElement:
        return self._wait_for(expected_condition=EC.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        return self._wait_for(expected_condition=EC.element_to_be_clickable)

    def wait_for_visible(self) -> WebElement:
        return self._wait_for(expected_condition=EC.visibility_of_element_located)

    def is_exists(self) -> bool:
        try:
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def is_displayed(self) -> bool:
        try:
            self.wait_for_visible()
            return True
        except TimeoutException:
            return False

    def click(self):
        element = self.wait_for_clickable()
        Logger.info(f"{self}: click")
        try:
            element.click()
        except TimeoutException as err:
            Logger.error(f"{self}:{err}")
            raise

    def js_click(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script("arguments[0].click();", element)

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get text")
        try:
            text = element.text
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: text = '{text}'")
        return text

    def get_attribute(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get attribute '{name}'")
        try:
            value = element.get_attribute(name)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute '{name}' = '{value}'")
        return value

    def get_css_property(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get css property '{name}'")
        try:
            value = element.value_of_css_property(name)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute '{name}' = '{value}'")
        return value

    def hover(self):
        element = self.wait_for_visible()
        ActionChains(self.browser.driver).move_to_element(element).perform()
        Logger.info(f"{self}: hover")
        return self\

    def scroll_to_element(self):
        Logger.info(f"{self}: scroll to element")
        return self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.wait_for_visible())


