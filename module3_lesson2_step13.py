from selenium import webdriver
import time
import unittest


class TestWeb(unittest.TestCase):
    def testOne(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        FirstName = browser.find_element_by_class_name('first_block .first')
        FirstName.send_keys("Ruslan")
        LastName = browser.find_element_by_class_name('first_block .second')
        LastName.send_keys("Usmanov")
        Email = browser.find_element_by_class_name('first_block .third')
        Email.send_keys("rus@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Texts must be the same")
        browser.close()
        browser.quit()

    def testTwo(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        FirstName = browser.find_element_by_class_name('first_block .first')
        FirstName.send_keys("Ruslan")
        LastName = browser.find_element_by_class_name('first_block .second')
        LastName.send_keys("Usmanov")
        Email = browser.find_element_by_class_name('first_block .third')
        Email.send_keys("rus@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Texts must be the same")
        # закрываем браузер после всех манипуляций
        browser.close()
        browser.quit()


if __name__ == "__main__":
    unittest.main()
