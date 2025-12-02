import pytest
from utils.driver_singleton import DriverSingleton

@pytest.fixture
def driver():
    driver_instance = DriverSingleton.get_driver()
    yield driver_instance
    DriverSingleton.close_driver()
