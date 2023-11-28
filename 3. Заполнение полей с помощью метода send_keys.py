import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
  driver = webdriver.Chrome()
  link = 'https://www.saucedemo.com/'
  driver.get(link)
  username = driver.find_element(By.ID, "user-name") #поиск по ID
  username.send_keys("standard_user") #Отправка данных в поле
  password = driver.find_element(By.CSS_SELECTOR, '#password')
  password.send_keys('standart_password')

finally:
  time.sleep(3)
  driver.close()
