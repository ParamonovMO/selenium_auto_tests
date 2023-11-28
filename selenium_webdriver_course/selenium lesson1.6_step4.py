# Переход, заполнение полей ввода и клик по кнопке на форме регистрации

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'
driver = webdriver.Chrome()
driver.get(link)
try:
    first_name = driver.find_element(By.NAME, 'first_name')
    first_name.send_keys('Максим')

    last_name = driver.find_element(By.NAME, 'last_name')
    last_name.send_keys('Парамонов')

    city = driver.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Пермь')

    country = driver.find_element(By.ID, 'country')
    country.send_keys('Россия')

    button = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(25)
    driver.quit()
