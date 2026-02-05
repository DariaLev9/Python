from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

btn_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(btn_text)

driver.quit()
