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
# text_products = driver.find_element(By.XPATH, "//span [text()='Products']")
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "Products"
# print("Good")

  url = "https://www.saucedemo.com/inventory.html"
  get_url = driver.current_url
  print(get_url)
  assert url == get_url #проверка совпадения текущего URL 
  print("Good url") 

finally:
  time.sleep(3)
  driver.close()
