from selenium import webdriver 
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://www.google.com")
print("page title:",driver.title)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("selenium webdriver")
search_box.submit()
print("result page title",driver.title)
driver.quit()