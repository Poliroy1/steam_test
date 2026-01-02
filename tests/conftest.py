import os
import pytest
from core.browser import Browser
from core.config_reader import ConfigReader
from logger.logger import Logger
from core.browser_factory import BrowserFactory

@pytest.fixture(scope="session")
def config():
    return ConfigReader()

@pytest.fixture(scope="session")
def base_url(config):
    return config.get("base_url")

@pytest.fixture(scope="session", autouse=True)
def prepare_logs():
    os.makedirs("logs", exist_ok=True)

@pytest.fixture
def browser(config):
    options = []
    if config.get("headless", False):
        options.append("--headless")

    driver = BrowserFactory.get_driver(options=options)
    browser = Browser(driver)

    yield browser
    browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        Logger.error(f"Test failed: {item.name}")