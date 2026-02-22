from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver, timeout=50):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value: str):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(value)

    def click(self, text: str):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def calculate_7_plus_8(self):
        self.click("7")
        self.click("+")
        self.click("8")
        self.click("=")

    def wait_result_is(self, expected_text: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_text))

    def get_result_text(self) -> str:
        return self.driver.find_element(*self.screen).text
