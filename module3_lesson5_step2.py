import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")  #“function”, “class”, “module”, “session”.
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")