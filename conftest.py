import pytest
from selenium import webdriver


@pytest.fixture(scope="function")  # “function”, “class”, “module”, “session”.
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("Quit browser...")
    browser.close()
    browser.quit()
