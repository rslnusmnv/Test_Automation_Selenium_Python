import pytest
from selenium import webdriver
import time
import math






class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    @pytest.mark.parametrize('link',
                             ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                              "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                              "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                              "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def testOne(self, browser, link):
        print("Start test...")
        browser.get(link)
        answer = math.log(int(time.time()))
        input_field = browser.find_element_by_class_name("ember-text-area.ember-view.textarea.string-quiz__textarea")
        input_field.send_keys(str(answer))
        submit_button = browser.find_element_by_class_name("submit-submission")
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        textLabel = browser.find_element_by_class_name("smart-hints__hint")
        actual_result = textLabel.text
        expected_result = "Correct!"
        assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
        print("Finish test...")
