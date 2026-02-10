from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Дарья")
        driver.find_element(By.ID, "last-name").send_keys("Левченкова")
        driver.find_element(By.ID, "postal-code").send_keys("123123")
        driver.find_element(By.ID, "continue").click()

        total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))).text
        assert "$58.29" in total

    finally:
        driver.quit()
