from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def add_sauce_labs_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.add_backpack)).click()

    def add_sauce_labs_bolt_t_shirt(self):
        self.driver.find_element(*self.add_bolt_tshirt).click()

    def add_sauce_labs_onesie(self):
        self.driver.find_element(*self.add_onesie).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
