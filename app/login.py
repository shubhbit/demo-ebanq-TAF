import pytest
from selenium import webdriver
from app.login_locators import Login_Locators

from common.utility import wait_for_element_load, wait


class Login(object):
    def __init__(self):
        self.timeout = 10
        self.bank_url = (pytest.config['BANK_URL']).replace("\n", "")
        self.driver = webdriver.Firefox()
        self.driver.get(self.bank_url)
        assert wait_for_element_load(
            self.driver, self.timeout, Login_Locators.SIGN_IN_BUTTON_LOCATOR)

    def enter_username(self, user):
        if wait_for_element_load(self.driver, self.timeout, Login_Locators.USER_TEXT_LOCATOR):
            email = self.driver.find_element(*Login_Locators.USER_TEXT_LOCATOR)
            email.send_keys(user)
        else:
            raise Exception("Element: {} not found".format(
                Login_Locators.USER_TEXT_LOCATOR))

    def enter_password(self, password):
        if wait_for_element_load(self.driver, self.timeout, Login_Locators.PASSWORD_TEXT_LOCATOR):
            password_text = self.driver.find_element(
                *Login_Locators.PASSWORD_TEXT_LOCATOR)
            password_text.send_keys(password)
        else:
            raise Exception("Element: {} not found".format(
                Login_Locators.PASSWORD_TEXT_LOCATOR))

    def click_sign_in_button(self):
        if wait_for_element_load(self.driver, self.timeout, Login_Locators.SIGN_IN_BUTTON_LOCATOR):
            sign_in_button = self.driver.find_element(
                *Login_Locators.SIGN_IN_BUTTON_LOCATOR)
            sign_in_button.click()
        else:
            raise Exception("Element: {} not found".format(
                Login_Locators.SIGN_IN_BUTTON_LOCATOR))

    def login(self, user, password):
        self.enter_username(user)
        self.enter_password(password)
        self.click_sign_in_button()

    def verify_login_successful(self):
        if wait_for_element_load(self.driver, self.timeout, Login_Locators.SUCCESS_ALERT):
            return "Hello" in self.driver.page_source
        else:
            raise Exception("Element: {} not found".format(
                Login_Locators.SUCCESS_ALERT))

    def verify_graceful_error(self):
        wait(2)
        return "Wrong username or password." in self.driver.page_source

    def close_driver(self):
        self.driver.close()
