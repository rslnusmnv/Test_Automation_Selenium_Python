from selenium import webdriver
import time
import math
import os

try:
    with open("file.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Ruslan")
    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys("Usmanov")
    Email = browser.find_element_by_name("email")
    Email.send_keys("rus@gmail.com")
    File = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    File.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
