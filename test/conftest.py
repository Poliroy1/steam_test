import pytest
from utils.driver_singleton import DriverSingleton

@pytest.fixture
def driver(lang):
    driver_instance = DriverSingleton.get_driver(lang)
    yield driver_instance
    DriverSingleton.close_driver()