from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# link = 'https://suninjuly.github.io/selects1.html'
link = 'https://suninjuly.github.io/selects2.html'
driver = webdriver.Chrome()

driver.get(link)

num1 = driver.find_element(By.ID, 'num1')
x = int(num1.text)
num2 = driver.find_element(By.ID, 'num2')
y = int(num2.text)

summa = str(x + y)
print(summa)

select = Select(driver.find_element(By.TAG_NAME, 'select'))
select.select_by_value(summa)

btn = driver.find_element(By.TAG_NAME, 'button')
btn.click()

time.sleep(15)
driver.quit()
