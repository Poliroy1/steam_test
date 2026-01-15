import pytest
from browser.browser_factory import BrowserFactory
from browser.browser import Browser
from browser.config_reader import ConfigReader
from logger.logger import Logger


@pytest.fixture
def browser():
    config = ConfigReader.load_config()
    browser_cfg = config["browser"]

    driver = BrowserFactory.get_driver(browser_cfg.get("options", []))
    browser = Browser(driver)
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        Logger.error(f"Test failed: {item.name}")
