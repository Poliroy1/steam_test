import pytest
from browser.browser_factory import BrowserFactory
from browser.browser import Browser
from logger.logger import Logger

# ----------------------------
# Фикстура браузера на всю сессию
# ----------------------------
@pytest.fixture
def browser():
    # Просто создаём драйвер через фабрику
    driver = BrowserFactory.get_driver()  # без лишних параметров

    # Оборачиваем в наш Browser — таймауты и page_load_timeout уже внутри класса Browser
    browser = Browser(driver)

    Logger.info("Browser started")
    yield browser

    Logger.info("Browser quitting")
    browser.quit()
# ----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    # Если тест упал на этапе выполнения
    if rep.when == "call" and rep.failed:
        Logger.error(f"Test failed: {item.name}")
