import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    elem = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    btn = browser.find_element(By.ID, "book")
    btn.click()

    x = browser.find_element(By.ID, 'input_value').text
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x))

    button = browser.find_element(By.ID, "solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(": ")[-1])

finally:
    time.sleep(5)
    browser.quit()

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait2.html")
#
#
# btn = WebDriverWait(browser, 5).until(
#     EC.element_to_be_clickable((By.ID, "verify"))
# )
# btn.click()
#
# msg = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in msg.text
