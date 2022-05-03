from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector('[type="text"]')
    for element in elements:
        element.send_keys("Kek")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    assert len(button) == 100

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    browser.close()
    browser.quit()

