import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture
def browser():
    print("\nПоехали!")
    browser = webdriver.Chrome()
    yield browser
    print("\nПриехали!!")
    browser.quit()


links_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize("links", links_list)
def test_quest_should_see_login_link(browser, links):
    link = f"{links}"
    browser.get(link)

    input1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
    answer = str(math.log(int(time.time() + 0.7)))
    input1.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    res = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    if res != "Correct!":
        print(res)


