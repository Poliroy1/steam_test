from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = 'https://store.steampowered.com/'
    LOGO = (By.XPATH, "//*[@type='submit']")
    SEARCH = (By.XPATH, "//*[@role='combobox']")
    SEARCH_BUTTON = (By.XPATH, "//*[@type='submit']")
    UNIQUE = (By.XPATH, "//*[@id='term']")

    def __init__(self, driver, TIMEOUT=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self, url=None):
        if url is None:
            url = self.URL
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located(self.LOGO))

    def search_game(self, name):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH)).send_keys(name)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE))