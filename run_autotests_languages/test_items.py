import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_run_auto_different_interface_languages(browser):
    browser.get(link)
    time.sleep(30)

    bt_lst = browser.find_elements(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')

    assert len(bt_lst) > 0, "Help"
