from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        self.wait.until(
            EC.visibility_of_element_located(self.username_input)
            ).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login_as(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
