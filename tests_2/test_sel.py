from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_singleton import DriverSingleton



URL = 'https://store.steampowered.com/'
LOGO = (By.XPATH, "//*[@type='submit']")
SEARCH = (By.XPATH, "//*[@role='combobox']")
SEARCH_BUTTON = (By.XPATH, "//*[@type='submit']")
SORTER = (By.XPATH, "//*[@id='sort_by_trigger']")
FILTER = (By.XPATH, "//*[@id='Price_DESC']")
UNIQUE = (By.XPATH, "//*[@id='term']")
SEARCH_RESULT = (By.XPATH, "//*[@id='search_result_container']")
GAMES_PRICE = (By.XPATH, "//*[contains(@class,'search_price_discount_combined')]")



GAME_ONE = 'The Witcher'
N = 10

TIMEOUT = 30


def test_second():
    wait = WebDriverWait(driver, TIMEOUT)
#1
    driver.get(URL)
    wait.until(EC.presence_of_element_located(LOGO))
#2-3
    wait.until(EC.visibility_of_element_located(SEARCH)).send_keys(GAME_ONE)
    wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(UNIQUE))

    old_result = wait.until(EC.presence_of_element_located(SEARCH_RESULT))
#4
    wait.until(EC.element_to_be_clickable(SORTER)).click()
    wait.until(EC.element_to_be_clickable(FILTER)).click()
    wait.until(EC.staleness_of(old_result))
#5
    wait.until(EC.presence_of_element_located(SEARCH_RESULT))
    elements = wait.until(EC.presence_of_all_elements_located(GAMES_PRICE))

    prices_list = [int(element.get_attribute("data-price-final")) for element in elements[:N]]

    assert prices_list == sorted(prices_list, reverse=True)




