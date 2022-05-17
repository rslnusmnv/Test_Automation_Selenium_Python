import pytest
from selenium import webdriver
import time
import math


class TestMainPage1():
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_add_to_cart_button_is_displayed(self, browser):
        print("Start test...")
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        addToBasket_button = browser.find_elements_by_class_name("btn-add-to-basket")
        assert len(addToBasket_button) < 0, "Button is not found"
        print("Finish test...")