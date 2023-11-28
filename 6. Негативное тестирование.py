import time
from selenium import webdriver
from selenium.webdriver.common.by import By

login_standard_user = "standard_user"
password_all = "secret_sauce123"

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
  
#Создаём переменную с найденным элементом
  warning_text = driver.find_element(By.TAG_NAME, "h3")
#Создаём новую переменную value_warning_text, которой присваеим переменную warning_text с методом text
  value_warning_text = warning_text.text
#Сравниваем переменную value_warring_text с отображаемой ошибкой
  assert value_warning_text == "Epic sadface: Username and password do not match any user in this service"
  print("Good Test")

finally:
  time.sleep(3)
  driver.close()