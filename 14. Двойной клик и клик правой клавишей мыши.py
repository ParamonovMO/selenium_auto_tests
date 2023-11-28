import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

try:
  driver = webdriver.Chrome()
  link = 'https://demoqa.com/buttons'
  driver.get(link)

  action = ActionChains(driver)
  double = driver.find_element(By.CSS_SELECTOR, "#doubleClickBtn")
  action.double_click(double).perform() # метод perform сохраняет результат
  print("Click DoubleClick Button")

  right_click = driver.find_element(By.CSS_SELECTOR, "#rightClickBtn")
  action.context_click(right_click).perform()
  print("Click RightClick Button")

  click = driver.find_element(By.XPATH, "//button[@id='FDEr6']")
  click.click()
  print("Click Button")

finally:
  time.sleep(1)
  driver.close()
