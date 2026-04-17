from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url


def test_login_invalid_user(driver):
    login = LoginPage(driver)
    login.open()
    login.login("fake_user", "fake_password")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
    )
    assert error.is_displayed()


def test_login_empty_fields(driver):
    login = LoginPage(driver)
    login.open()
    login.login("", "")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
    )
    assert error.is_displayed()
