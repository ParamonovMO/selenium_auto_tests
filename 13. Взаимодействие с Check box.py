import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
  driver = webdriver.Chrome()
  link = 'https://demoqa.com/checkbox'
  driver.get(link)

  check_box = driver.find_element(By.CLASS_NAME, "rct-icon")
  check_box.click()
  print("Click Checkbox")

  toggle_button = driver.find_element(By.CSS_SELECTOR, "[title='Toggle']")
  toggle_button.click()
  print("Click Toggle Button")

finally:
  time.sleep(1)
  driver.close()