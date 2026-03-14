import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """
    Класс страницы списка товаров.

    Содержит методы для добавления товаров в корзину
    и перехода к странице корзины.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализирует страницу товаров.

        :param driver: Экземпляр WebDriver.
        :param timeout: Максимальное время ожидания элементов.
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CSS_SELECTOR, "a.shopping_cart_link")

    @allure.step("Добавить товар Sauce Labs Backpack в корзину")
    def add_sauce_labs_backpack(self) -> None:
        """
        Добавляет товар Sauce Labs Backpack в корзину.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.add_backpack)
        ).click()

    @allure.step("Добавить товар Sauce Labs Bolt T-Shirt в корзину")
    def add_sauce_labs_bolt_t_shirt(self) -> None:
        """
        Добавляет товар Sauce Labs Bolt T-Shirt в корзину.

        :return: None
        """
        self.driver.find_element(*self.add_bolt_tshirt).click()

    @allure.step("Добавить товар Sauce Labs Onesie в корзину")
    def add_sauce_labs_onesie(self) -> None:
        """
        Добавляет товар Sauce Labs Onesie в корзину.

        :return: None
        """
        self.driver.find_element(*self.add_onesie).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        :return: None
        """
        self.driver.find_element(*self.cart_link).click()
