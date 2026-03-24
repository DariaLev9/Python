import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Класс страницы авторизации.

    Содержит методы для открытия страницы входа,
    ввода логина и пароля, а также авторизации пользователя.
    """

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализирует страницу авторизации.

        :param driver: Экземпляр WebDriver.
        :param timeout: Максимальное время ожидания элементов.
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """
        self.driver.get(self.URL)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле логина.

        :param username: Имя пользователя.
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле пароля.

        :param password: Пароль пользователя.
        :return: None
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа.

        :return: None
        """
        self.driver.find_element(*self.login_button).click()

    @allure.step("Авторизоваться пользователем {username}")
    def login_as(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему с указанными учетными данными.

        :param username: Имя пользователя.
        :param password: Пароль пользователя.
        :return: None
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
