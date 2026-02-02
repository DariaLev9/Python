from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Ввод username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Ввод password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Клик по кнопке Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(1)

# Получить текст с зеленой плашки и вывести в консоль
message = driver.find_element(By.ID, "flash").text
print(message)

# Закрыть браузер
driver.quit()
