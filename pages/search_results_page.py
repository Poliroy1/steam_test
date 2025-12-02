from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

cfg = ConfigReader()

class SearchResultsPage:
    SORTER = (By.ID, "sort_by_trigger")
    FILTER = (By.ID, "Price_DESC")
    SEARCH_RESULT = (By.ID, "search_result_container")
    GAMES_PRICE = (By.XPATH, "//*[contains(@class,'search_price_discount_combined')]")
    ERROR = (By.XPATH, "//*[@aria-activedescendant = 'Released_DESC']")

    def __init__(self, driver, TIMEOUT=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT or cfg.timeout)

    def apply_price_filter(self):
        self.wait.until(EC.element_to_be_clickable(self.SORTER)).click()
        self.wait.until(EC.element_to_be_clickable(self.FILTER)).click()
        self.wait.until(EC.invisibility_of_element_located(self.ERROR))


    def get_prices(self, n):
        self.wait.until(EC.presence_of_element_located(self.SEARCH_RESULT))
        elements = self.wait.until(EC.presence_of_all_elements_located(self.GAMES_PRICE))
        prices = []
        for i in elements:
            price_str = i.get_attribute("data-price-final")
            if price_num := int(price_str) >= 0:
                prices.append(price_num)
            if len(prices) == n:
                break

        return prices

