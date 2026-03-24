import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.title("Проверка калькулятора: 7 + 8 = 15")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с задержкой выполнения операции.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_02_calc_page_object():
    """
    Тест проверяет, что калькулятор корректно выполняет операцию 7 + 8
    с установленной задержкой.
    """
    driver = webdriver.Chrome()

    try:
        page = CalculatorPage(driver, timeout=50)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay("45")

        with allure.step("Выполнить вычисление 7 + 8"):
            page.calculate_7_plus_8()

        with allure.step("Дождаться результата 15"):
            page.wait_result_is("15")

        with allure.step("Получить результат с экрана"):
            result = page.get_result_text()

        with allure.step("Проверить результат"):
            assert result == "15", f"Ожидалось 15, получено {result}"

    finally:
        driver.quit()
