from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def add_first_product(self):
        self.wait_for_element((By.CSS_SELECTOR, ".inventory_item button")).click()

    def get_cart_count(self):
        return self.wait_for_element((By.CLASS_NAME, "shopping_cart_badge")).text