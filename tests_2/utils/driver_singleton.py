from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverSingleton:
    _instance = None
    _driver = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_driver(self):
        if self._driver is None:
            service = Service(ChromeDriverManager().install())
            self._driver = webdriver.Chrome(service=service)
            self._driver.implicitly_wait(10)
        return self._driver

    def close_driver(self):
        if self._driver:
            self._driver.quit()
            self._driver = None