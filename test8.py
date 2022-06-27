from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element(By.ID, 'num1')
    x = n1.text
    n2 = browser.find_element(By.ID, 'num2')
    y = n2.text
    res = int(x) + int(y)
    select1 = Select(browser.find_element(By.TAG_NAME, 'select'))
    select1.select_by_value(str(res))

    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
