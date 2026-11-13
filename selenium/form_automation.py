
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_box = driver.find_element(By.ID, "my-text-id")
text_box.send_keys("Hello Selenium!")

submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

message = driver.find_element(By.ID, "message")
print("Result:", message.text)

# Wait for 5 seconds
time.sleep(5)

driver.quit()
