from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

image_3 = driver.find_element(By.XPATH, "(//img)[3]")

print(image_3.get_attribute("src"))

driver.quit()
