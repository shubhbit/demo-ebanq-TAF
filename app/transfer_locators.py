from selenium.webdriver.common.by import By


class Transfer_Locators(object):
    TRANSFER_LINK_LOCATOR = (By.XPATH, "//div[@routerlink='/transfer']")
    TRANSFER_BET_ACCOUNTS_LOCATOR = (
        By.XPATH, "//div[@ng-reflect-router-link='admin/transfer-between-account']")
    SELECT_USER_LOCATOR = (
        By.XPATH, "//ng-select[@ng-reflect-placeholder='Select a user']//input[@role='combobox']")
    USER_OPTION_LOCATOR = (
        By.XPATH, "//div[@role='option'][normalize-space(.)='{}']")
    ACCOUNT_FROM_LOCATOR = (
        By.XPATH, "//app-account-select[@ng-reflect-name='accountFrom']//ng-select")
    OPTION_LOCATOR = (By.XPATH, "//div[@role='option']")
    ACCOUNT_TO_LOCATOR = (
        By.XPATH, "//app-account-select[@ng-reflect-name='accountTo']//ng-select")
    AMOUNT_LOCATOR = (By.XPATH, "//input[@formcontrolname='outgoingAmount']")
    DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, "textarea#description")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    SUCCESS_LOCATOR = (By.CSS_SELECTOR, "div.success-popup")
