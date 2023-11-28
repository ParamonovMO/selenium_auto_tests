# Переход, заполнение формы, поиск кнопки с помощью XPath и клик по ней

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_xpath_form'
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

    button = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[6]/button[3]").click()

finally:
    time.sleep(25)
    driver.quit()
