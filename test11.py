from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(": ")[-1])


finally:
    time.sleep(10)
    browser.quit()
