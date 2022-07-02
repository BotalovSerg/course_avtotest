import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    # print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n", "^_^", "\n")
    yield
    print("\n", ":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print("\n", ":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n", ":-Р", "\n")


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser, prepare_faces, very_important_fixture):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser, prepare_faces):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
