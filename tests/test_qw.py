import faker
import pytest
from faker import Faker
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://store.steampowered.com/"
LOGO = By.XPATH, "//*[@placeholder='Поиск по магазину']"
QR_LOGO = By.XPATH, "//*[@style='position: relative;']//img"
BUTTON_LOGIN = By.XPATH, "//*[@class='global_action_link' and contains(@href, '/login/')]"
USERNAME_INPUT = By.XPATH, "//input[@type='text' and contains(@class, 'Weup5')]"
PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
BUTTON_LOGOUT = By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]"

ERROR_TEXT = By.XPATH, "//*[text() = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.']"

faker = Faker()

random_username = faker.user_name()
random_password = faker.password()

def test_first(driver):
    wait = WebDriverWait(driver, 30)

    driver.get(URL)

    wait.until(EC.presence_of_element_located(LOGO))
    #кнопка войти
    wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    wait.until(EC.presence_of_element_located(QR_LOGO))

    wait.until(EC.visibility_of_element_located(USERNAME_INPUT)).send_keys(random_username)

    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(random_password)

    wait.until(EC.element_to_be_clickable(BUTTON_LOGOUT)).click()

    er = wait.until(EC.visibility_of_element_located(ERROR_TEXT))

    er_q = er.text

    er_txt = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'

    assert er_q == er_txt

    time.sleep(5)