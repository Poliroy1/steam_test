from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader


class DriverSingleton:
    _driver = None

    @classmethod
    def get_driver(cls, lang=None):
        if cls._driver is None:
            config = ConfigReader()

            if lang is None:
                lang = config.languages[0] if config.languages else "en"

            options = webdriver.ChromeOptions()
            if config.browser_setting("lang_in_options", False):
                options.add_experimental_option("prefs", {"intl.accept_languages": lang})
                options.add_argument(f"--lang={lang}")

            service = Service(ChromeDriverManager().install())
            cls._driver = webdriver.Chrome(service=service, options=options)

        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
