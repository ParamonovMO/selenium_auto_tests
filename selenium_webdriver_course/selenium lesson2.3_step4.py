from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
driver = webdriver.Chrome()
driver.get(link)

btn = driver.find_element(By.TAG_NAME, 'button').click()

confirm = driver.switch_to.alert.accept()

x = driver.find_element(By.CSS_SELECTOR, '#input_value').text


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)

input = driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
btn2 = driver.find_element(By.TAG_NAME, 'button').click()

time.sleep(12)
