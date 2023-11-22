from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(
        By.XPATH, '//body/div[1]/form[1]/div[1]/div[1]/input[1]')
    first_name.send_keys('Максим')

    last_name = driver.find_element(
        By.XPATH, '//body/div[1]/form[1]/div[1]/div[2]/input[1]')
    last_name.send_keys('Парамонов')

    email = driver.find_element(
        By.XPATH, '//body/div[1]/form[1]/div[1]/div[3]/input[1]')
    email.send_keys('123@ya.ru')

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    driver.quit()
