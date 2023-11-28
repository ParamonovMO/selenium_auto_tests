import time
from selenium import webdriver

driver = webdriver.Chrome() #определяем драйвер хром
link = 'https://www.saucedemo.com/' #присваиваем ссылку
try: 
  driver.get(link) #переход по ссылке
finally:
  time.sleep(3) #время ожидания 
  driver.close() #закрытие брайзера
