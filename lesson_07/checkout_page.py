from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, "[data-test='total-label']")

    def fill_first_name(self, value: str):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)).send_keys(value)

    def fill_last_name(self, value: str):
        self.driver.find_element(*self.last_name).send_keys(value)

    def fill_postal_code(self, value: str):
        self.driver.find_element(*self.postal_code).send_keys(value)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def fill_form_and_continue(self, first: str, last: str, zip_code: str):
        self.fill_first_name(first)
        self.fill_last_name(last)
        self.fill_postal_code(zip_code)
        self.click_continue()

    def get_total_text(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self.total_label)).text
