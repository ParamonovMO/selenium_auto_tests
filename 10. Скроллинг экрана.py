import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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

#Скроллим по экрану по оси X - горизонталь, Y - вертикаль
# driver.execute_script("window.scrollTo(0, 500)")
#Создаём переменную, с помощью которой можем управлять драйвером
  action = ActionChains(driver)
#Создаём переменную и находим нужный элемент"""
  red_t_shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
#перемещаемся к данному элементу"""
  action.move_to_element(red_t_shirt).perform()

  name_screenshot = "screenshot" + '.png'

  driver.save_screenshot('C:\\Autotesting_python_selenium_stepik\\4. Базовый курс Selenium\\screenshots\\' + name_screenshot)

finally:
  time.sleep(3)
  driver.close()