
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open practice website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Find text box
text_box = driver.find_element(By.ID, "my-text-id")

# Enter text
text_box.send_keys("Hello Selenium!")

# Find and click submit button
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

# Display result
message = driver.find_element(By.ID, "message")
print("Result:", message.text)

# Close browser
driver.quit()
