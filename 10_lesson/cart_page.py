import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Класс страницы корзины.

    Содержит методы для взаимодействия с корзиной:
    получения товаров и перехода к оформлению заказа.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр WebDriver.
        :param timeout: Максимальное время ожидания элементов.
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.checkout_button = (By.ID, "checkout")
        self.item_names = (By.CSS_SELECTOR, ".inventory_item_name")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    @allure.step("Получить список товаров в корзине")
    def get_cart_item_names(self) -> list[str]:
        """
        Возвращает список названий товаров в корзине.

        :return: Список названий товаров.
        """
        elements = self.driver.find_elements(*self.item_names)
        return [el.text for el in elements]
