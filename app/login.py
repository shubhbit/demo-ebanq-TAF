import pytest
from selenium import webdriver
from app.login_locators import Login_Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login(object):
    def __init__(self):
        self.bank_url = (pytest.config['BANK_URL']).replace("\n", "")
        self.driver = webdriver.Firefox()
        self.driver.get(self.bank_url)

    def login(self, user, password):
        email = self.driver.find_element(
            By.XPATH, Login_Locators.USER_TEXT_LOCATOR)
        email.send_keys(user)
        password = self.driver.find_element(
            By.XPATH, Login_Locators.PASSWORD_TEXT_LOCATOR)
        password.send_keys(password)
        sign_in_button = self.driver.find_element(
            By.XPATH, Login_Locators.SIGN_IN_BUTTON_LOCATOR)
        sign_in_button.click()
