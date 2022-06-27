from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print(robots_checked)
    assert robots_checked is None

    # x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    # x = x_element.text
    # print(x)
    # y = calc(x)
    # print(y)
    #
    # input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    # input1.send_keys(y)
    # checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    # checkbox.click()
    #
    # radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    # radio.click()
    #
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
