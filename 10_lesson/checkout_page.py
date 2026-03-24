import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Класс страницы оформления заказа.

    Содержит методы для заполнения формы пользователя
    и получения итоговой стоимости заказа.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализирует страницу оформления заказа.

        :param driver: Экземпляр WebDriver.
        :param timeout: Максимальное время ожидания элементов.
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, "[data-test='total-label']")

    @allure.step("Ввести имя: {value}")
    def fill_first_name(self, value: str) -> None:
        """
        Заполняет поле имени.

        :param value: Имя пользователя.
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(value)

    @allure.step("Ввести фамилию: {value}")
    def fill_last_name(self, value: str) -> None:
        """
        Заполняет поле фамилии.

        :param value: Фамилия пользователя.
        :return: None
        """
        self.driver.find_element(*self.last_name).send_keys(value)

    @allure.step("Ввести почтовый индекс: {value}")
    def fill_postal_code(self, value: str) -> None:
        """
        Заполняет поле почтового индекса.

        :param value: Почтовый индекс.
        :return: None
        """
        self.driver.find_element(*self.postal_code).send_keys(value)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа.

        :return: None
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Заполнить форму пользователя")
    def fill_form_and_continue(
        self,
        first: str,
        last: str,
        zip_code: str
    ) -> None:
        """
        Заполняет форму пользователя и продолжает оформление заказа.

        :param first: Имя пользователя.
        :param last: Фамилия пользователя.
        :param zip_code: Почтовый индекс.
        :return: None
        """
        self.fill_first_name(first)
        self.fill_last_name(last)
        self.fill_postal_code(zip_code)
        self.click_continue()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total_text(self) -> str:
        """
        Возвращает текст итоговой стоимости заказа.

        :return: Текст итоговой стоимости.
        """
        return self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        ).text
