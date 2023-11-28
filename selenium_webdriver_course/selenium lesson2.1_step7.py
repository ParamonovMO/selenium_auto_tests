from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'


def fn(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver.get(link)
    x = int(driver.find_element(By.ID, 'treasure').get_attribute('valuex'))

    result = fn(x)
    input_text = driver.find_element(By.XPATH, "//input[@id='answer']")
    input_text.send_keys(result)
    chek = driver.find_element(By.ID, 'robotCheckbox').click()
    radio = driver.find_element(By.ID, 'robotsRule').click()
    button = driver.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(25)
    driver.quit()
