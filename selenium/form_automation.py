
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(2)

text_box = driver.find_element(By.ID, "my-text-id")

# Type slowly
text = "Hello Selenium!"

for character in text:
    text_box.send_keys(character)
    time.sleep(0.3)

time.sleep(2)

submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

time.sleep(3)

message = driver.find_element(By.ID, "message")
print("Result:", message.text)

time.sleep(5)

driver.quit()
