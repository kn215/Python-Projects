from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucelabs.com/")

# Using IDs (best practice)
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
time.sleep(15)
driver.find_element(By.XPATH, "//span[text()='Pricing']").click()

# Wait so you can see results
time.sleep(40)


driver.quit()




