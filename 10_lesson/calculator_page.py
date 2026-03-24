import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """
    Класс страницы калькулятора.

    Содержит методы для открытия страницы, ввода задержки,
    нажатия кнопок и получения результата вычисления.
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver: WebDriver, timeout: int = 50) -> None:
        """
        Инициализирует страницу калькулятора.

        :param driver: Экземпляр WebDriver.
        :param timeout: Максимальное время ожидания элементов в секундах.
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(self.URL)

    @allure.step("Установить задержку: {value}")
    def set_delay(self, value: str) -> None:
        """
        Устанавливает значение задержки для выполнения операции.

        :param value: Значение задержки в секундах.
        :return: None
        """
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(value)

    @allure.step("Нажать кнопку '{text}'")
    def click(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора по тексту.

        :param text: Текст кнопки.
        :return: None
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    @allure.step("Вычислить выражение 7 + 8")
    def calculate_7_plus_8(self) -> None:
        """
        Выполняет вычисление 7 + 8 на калькуляторе.

        :return: None
        """
        self.click("7")
        self.click("+")
        self.click("8")
        self.click("=")

    @allure.step("Дождаться результата: {expected_text}")
    def wait_result_is(self, expected_text: str) -> None:
        """
        Ожидает появления указанного результата на экране калькулятора.

        :param expected_text: Ожидаемый текст результата.
        :return: None
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_text)
        )

    @allure.step("Получить текст результата")
    def get_result_text(self) -> str:
        """
        Возвращает текст результата с экрана калькулятора.

        :return: Текст результата.
        """
        return self.driver.find_element(*self.screen).text
