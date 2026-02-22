from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.checkout_button = (By.ID, "checkout")

        self.item_names = (By.CSS_SELECTOR, ".inventory_item_name")

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)).click()

    def get_cart_item_names(self):
        elements = self.driver.find_elements(*self.item_names)
        return [el.text for el in elements]
