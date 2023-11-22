from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link_one = "http://suninjuly.github.io/registration1.html"
link_two = "http://suninjuly.github.io/registration2.html"


class Test_Registration(unittest.TestCase):
    def test_registration1(self):
        driver = webdriver.Chrome()
        driver.get(link_one)
        first_name = driver.find_element(
            By.TAG_NAME, 'input').send_keys('Максим')
        last_name = driver.find_element(
            By.XPATH, '//body/div[1]/form[1]/div[1]/div[2]/input[1]').send_keys('Парамонов')
        email = driver.find_element(
            By.XPATH, '//body/div[1]/form[1]/div[1]/div[3]/input[1]').send_keys('123@ya.ru')
        button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text
        print(welcome_text)
        self.assertEqual(
            welcome_text, "Congratulations! You have successfully registered!")

    def test_registration2(self):
        driver = webdriver.Chrome()
        driver.get(link_two)
        first_name = driver.find_element(
            By.TAG_NAME, 'input').send_keys('Максим')
        last_name = driver.find_element(
            By.XPATH, '//body/div[1]/form[1]/div[1]/div[2]/input[1]').send_keys('Парамонов')
        email = driver.find_element(
            By.XPATH, '//body/div[1]/form[1]/div[1]/div[3]/input[1]').send_keys('123@ya.ru')
        button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text
        print(welcome_text)
        self.assertEqual(
            welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
