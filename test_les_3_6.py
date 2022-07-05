import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

fin = ""


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    # ожидание прогрузки страницы
    browser.implicitly_wait(15)
    yield browser
    print(fin)


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
    global fin
    link = f"{links}"
    browser.get(link)

    input_1 = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer = str(math.log(int(time.time())))
    input_1.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()

    res = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    try:
        assert res == "Correct!"
    except AssertionError:
        fin += res
