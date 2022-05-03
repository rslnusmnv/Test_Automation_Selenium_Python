from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ruslan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Usmanov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Samara")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла