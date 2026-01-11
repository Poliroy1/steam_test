from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from logger.logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserFactory:
    @staticmethod
    def get_driver(
            options: list[str] = None,
    ) -> WebDriver:
        if options is None:
            options = []

        Logger.info(f"Запуск WebDriver 'chrome' с опциями: {options}")
        chrome_options = webdriver.ChromeOptions()

        for option in options:
            chrome_options.add_argument(option)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
