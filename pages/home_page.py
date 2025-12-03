from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

cfg = ConfigReader()

class HomePage:
    LOGO = (By.XPATH, "//*[@type='submit']")
    SEARCH = (By.XPATH, "//*[@role='combobox']")
    SEARCH_BUTTON = (By.XPATH, "//*[@type='submit']")
    UNIQUE = (By.ID, "term")

    def __init__(self, driver, TIMEOUT=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT or cfg.timeout)

    def wait_for_open(self):
        self.wait.until(EC.presence_of_element_located(self.LOGO))

    def search_game(self, name):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH)).send_keys(name)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE))