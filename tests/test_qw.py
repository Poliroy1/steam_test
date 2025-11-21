import faker
import pytest
from faker import Faker
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://store.steampowered.com/"
LOGO = (By.XPATH, "//*[@placeholder='Поиск по магазину']")
QR_LOGO = (By.XPATH, "//*[@id='responsive_page_template_content']//img")
BUTTON_LOGIN = (By.XPATH, "//*[@class='global_action_link' and contains(@href, '/login/')]")
USERNAME_INPUT = (By.XPATH, "//*[@id='responsive_page_template_content']//input[@type='text']")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
BUTTON_LOGOUT = (By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]")
LOADER = (By.XPATH, "//button[@type='submit' and @disabled]")

ERROR_TEXT = (By.XPATH, "//*[@id='responsive_page_template_content']//div[contains(text(), 'Пожалуйста, проверьте свой пароль')]")

faker = Faker()

RANDOM_USERNAME = faker.user_name()
RANDOM_PASSWORD = faker.password()

TIMEOUT = 30

def test_first(driver):
    wait = WebDriverWait(driver, TIMEOUT)

    driver.get(URL)

    wait.until(EC.presence_of_element_located(LOGO))
    #кнопка войти
    wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    wait.until(EC.presence_of_element_located(QR_LOGO))

    wait.until(EC.visibility_of_element_located(USERNAME_INPUT)).send_keys(RANDOM_USERNAME)

    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(RANDOM_PASSWORD)

    wait.until(EC.element_to_be_clickable(BUTTON_LOGOUT)).click()

    wait.until(EC.visibility_of_element_located(LOADER))

    wait.until(EC.invisibility_of_element_located(LOADER))

    er = wait.until(EC.visibility_of_element_located(ERROR_TEXT))

    actual_result = er.text

    expected_result = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'

    assert actual_result == expected_result, f'Ошибка валидации не соответствует ожидаемой. Expected: {expected_result}, Actual: {actual_result}'


