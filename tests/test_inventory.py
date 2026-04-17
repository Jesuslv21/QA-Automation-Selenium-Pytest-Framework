from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_inventory_loaded(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0


def test_sort_by_price(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("lohi")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_list = [float(p.text.replace("$", "")) for p in prices]

    assert price_list == sorted(price_list)
