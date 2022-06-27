# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # link = "http://suninjuly.github.io/simple_form_find_task.html"
# link = "http://suninjuly.github.io/find_xpath_form"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
# finally:
#     time.sleep(30)
#     browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//*[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, '//*[@id="country"]')
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

"""
Важное техническое замечание к работе selenium (особенно для тех кто пишет под windows (7,10)).
Дело в том что веб драйвер после окончания работы скрипты на самом деле не завершается окончательно, 
его нужно закрывать явным образом, самый простой способ это реализовать на Python, это использовать конструкцию try:

import time
from selenium import webdriver


try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера
    browser.get(link)


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    driver.close()
    time.sleep(2)
    driver.quit()

 

Блок finally будет выполнен в любом случае, даже если произойдет ошибка, 
по этому ваш веб драйвер всегда будет выгружаться из процессов а не висеть в них мёртвым грузом.
"""
