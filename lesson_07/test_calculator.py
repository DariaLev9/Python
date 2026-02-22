from selenium import webdriver
from calculator_page import CalculatorPage


def test_02_calc_page_object():
    driver = webdriver.Chrome()

    try:
        page = CalculatorPage(driver, timeout=50)

        page.open()
        page.set_delay("45")
        page.calculate_7_plus_8()

        page.wait_result_is("15")
        result = page.get_result_text()

        assert result == "15"

    finally:
        driver.quit()
