import pytest
from selenium import webdriver
from app.login_locators import Login_Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    def __init__(self):
        self.bank_url = (pytest.config['BANK_URL']).replace("\n", "")
        self.driver = webdriver.Firefox()
        # WebDriverWait(self.driver, 10).until(EC.)
        self.driver.get(self.bank_url)

    def enter_username(self, user):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, Login_Locators.USER_TEXT_LOCATOR)))
        email = self.driver.find_element(
            By.XPATH, Login_Locators.USER_TEXT_LOCATOR)
        email.send_keys(user)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, Login_Locators.PASSWORD_TEXT_LOCATOR)))
        password_text = self.driver.find_element(
            By.XPATH, Login_Locators.PASSWORD_TEXT_LOCATOR)
        password_text.send_keys(password)

    def click_sign_in_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, Login_Locators.SIGN_IN_BUTTON_LOCATOR)))
        sign_in_button = self.driver.find_element(
            By.XPATH, Login_Locators.PASSWORD_TEXT_LOCATOR)
        sign_in_button.click()

    def login(self, user, password):
        self.enter_username(user)
        self.enter_password(password)
        self.click_sign_in_button()

    def verify_login_successful(self):
        return "Hello" in self.driver.page_source

    def verify_graceful_error(self):
        return "Wrong username or password." in self.driver.page_source

    def close_driver(self):
        self.driver.close()
