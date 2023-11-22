# Поиск ссылки по тексту

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/find_link_text'
driver = webdriver.Chrome()
driver.get(link)

result = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    link_text = driver.find_element(By.LINK_TEXT, result).click()

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
