from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math
import time

driver = webdriver.Chrome()
link = 'https://SunInJuly.github.io/execute_script.html'


def fn(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver.get(link)
    x = driver.find_element(
        By.XPATH, '/html[1]/body[1]/div[1]/form[1]/div[1]/label[1]/span[2]').text

    input = driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(fn(x))

    check = driver.find_element(
        By.XPATH, "//input[@id='robotCheckbox']").click()
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ARROW_DOWN*5)

    radio = driver.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    btn = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(30)
    driver.quit()
