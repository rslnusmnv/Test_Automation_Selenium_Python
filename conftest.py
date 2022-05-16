import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")  # “function”, “class”, “module”, “session”.
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStart chrome browser for test...")
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test...")
        browser = webdriver.Firefox()
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("Quit browser...")
    browser.close()
    browser.quit()
