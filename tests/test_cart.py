from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_add_product(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert cart == "1"


def test_add_multiple_products(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    buttons = driver.find_elements(By.CSS_SELECTOR, ".inventory_item button")

    for i in range(3):
        buttons[i].click()

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart == "3"


def test_remove_product(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    btn = driver.find_element(By.CSS_SELECTOR, ".inventory_item button")
    btn.click()
    btn.click()

    cart = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart) == 0