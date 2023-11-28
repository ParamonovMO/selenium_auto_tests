import time
from selenium import webdriver
from selenium.webdriver.common.by import By

login_standard_user = "standard_user"
password_all = "secret_sauce"

try:
  driver = webdriver.Chrome()
  link = 'https://www.saucedemo.com/'
  driver.get(link)
  username = driver.find_element(By.CSS_SELECTOR, "#user-name")
  username.send_keys(login_standard_user)
  print("Input login")
  user_password = driver.find_element(By.CSS_SELECTOR, "#password")
  user_password.send_keys(password_all)
  print("Input password")
  button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
  button_login.click()
  print("Click login button")

  warning_text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
  value_warning_text = warning_text.text
  assert value_warning_text == "Epic sadface: Username and password do not match any user in this service"
  print("Good Test")
  
  driver.refresh() #Обновляем страницу
  print("Страница обновлена")

finally:
  time.sleep(3)
  driver.close()
