import allure
from selenium import webdriver

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Проверка итоговой суммы заказа")
@allure.description(
    "Тест проверяет корректность итоговой стоимости заказа "
    "после добавления товаров в корзину и оформления покупки."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_03_shop_total_page_object():
    """
    Тест выполняет полный пользовательский сценарий:
    авторизация → добавление товаров → оформление заказа →
    проверка итоговой стоимости.
    """
    driver = webdriver.Firefox()

    try:
        with allure.step("Открыть страницу авторизации и выполнить вход"):
            login_page = LoginPage(driver, timeout=10)
            login_page.open()
            login_page.login_as("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            inventory_page = InventoryPage(driver, timeout=10)
            inventory_page.add_sauce_labs_backpack()
            inventory_page.add_sauce_labs_bolt_t_shirt()
            inventory_page.add_sauce_labs_onesie()
            inventory_page.go_to_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page = CartPage(driver, timeout=10)
            cart_page.click_checkout()

        with allure.step("Заполнить форму покупателя"):
            checkout_page = CheckoutPage(driver, timeout=10)
            checkout_page.fill_form_and_continue(
                "Дарья", "Левченкова", "123123"
            )

        with allure.step("Получить итоговую стоимость заказа"):
            total_text = checkout_page.get_total_text()

        with allure.step("Проверить итоговую стоимость"):
            assert "$58.29" in total_text, (
                f"Ожидалась сумма $58.29, получено: {total_text}"
            )

    finally:
        driver.quit()
