# Передаем значения в каждый элемент списка

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    elements_list = driver.find_elements(By.TAG_NAME, 'input')
    for elem in elements_list:
        elem.send_keys('Привет')

    button = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(20)
    driver.quit()
