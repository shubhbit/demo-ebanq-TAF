from selenium.webdriver.common.by import By


class Login_Locators(object):
    USER_TEXT_LOCATOR = (By.XPATH, "//input[@type='email']")
    PASSWORD_TEXT_LOCATOR  = (By.XPATH, "//input[@type='password']")
    SIGN_IN_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    SUCCESS_ALERT = (By.CSS_SELECTOR , "div.greeting-bar")