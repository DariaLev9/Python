from selenium import webdriver

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_03_shop_total_page_object():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver, timeout=10)
        login_page.open()
        login_page.login_as("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver, timeout=10)
        inventory_page.add_sauce_labs_backpack()
        inventory_page.add_sauce_labs_bolt_t_shirt()
        inventory_page.add_sauce_labs_onesie()
        inventory_page.go_to_cart()

        cart_page = CartPage(driver, timeout=10)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver, timeout=10)
        checkout_page.fill_form_and_continue("Дарья", "Левченкова", "123123")

        total_text = checkout_page.get_total_text()
        assert "$58.29" in total_text

    finally:
        driver.quit()
