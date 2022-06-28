from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestWelcomeText(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//label[contains(text(),"First name")]/following-sibling::input')
        input1.send_keys("Serg")
        input2 = browser.find_element(By.XPATH, '//label[contains(text(),"Last name")]/following-sibling::input')
        input2.send_keys("Botalov")
        input3 = browser.find_element(By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')
        input3.send_keys("123@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        s1 = "Congratulations! You have successfully registered!"
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        self.assertEqual(s1, welcome_text, "Все пало")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//label[contains(text(),"First name")]/following-sibling::input')
        input1.send_keys("Serg")
        input2 = browser.find_element(By.XPATH, '//label[contains(text(),"Last name")]/following-sibling::input')
        input2.send_keys("Botalov")
        input3 = browser.find_element(By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')
        input3.send_keys("123@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        s1 = "Congratulations! You have successfully registered!"
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        self.assertEqual(s1, welcome_text, "Все пало")
