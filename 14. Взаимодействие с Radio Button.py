import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
  driver = webdriver.Chrome()
  link = 'https://demoqa.com/radio-button'
  driver.get(link)
  

  radio_button = driver.find_element(By.CSS_SELECTOR, "[for='yesRadio']")
  radio_button.click()
  print("Click Radio Button")

finally:
  time.sleep(1)
  driver.close()
