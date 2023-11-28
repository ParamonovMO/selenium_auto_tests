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
  print("Input Password")
  button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
  button_login.click()
  print("Click Login Button")

#Создаём переменную menu и находим её элемент
  menu = driver.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn")
  menu.click()
  print("Click Menu Button")
  time.sleep(1)
#Создаём переменную about и находим её элемент
  link_about = driver.find_element(By.CSS_SELECTOR, "#about_sidebar_link")
  link_about.click()
  print("Click Link Button")
finally:
  time.sleep(3)
  driver.close()
