import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
  driver = webdriver.Chrome()
  link = 'https://www.saucedemo.com/'
  driver.get(link)
# username = driver.find_element(By.ID, "user-name") #ID
# username = driver.find_element(By.NAME, "user-name") #NAME
# username = driver.find_element(By.XPATH, "//*[@id='user-name']") #FULL-XPATH
# username = driver.find_element(By.XPATH, "//input[@id='user-name']") #ID XPATH
# username = driver.find_element(By., "//input[@data-test='username']") #data-test XPATH
# username.send_keys("standard_user")

  username = driver.find_element(By.XPATH, "//input[@id='user-name']") #ID XPATH
  username.send_keys("standard_user")

  user_password = driver.find_element(By.CSS_SELECTOR, "#password") #ID CSS SELECTOR
  user_password.send_keys("secret_sauce")

  button_login = driver.find_element(By.ID, "login-button")
  button_login.click()
finally:
  time.sleep(3)
  driver.close()
