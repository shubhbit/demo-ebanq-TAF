from app.transfer_locators import Transfer_Locators
from app.login import Login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Transfer(Login):
    """
    Page object for Transfer web page
    """

    def __init__(self, user, password):
        """
        constructor method where Transfer page will be navigated
        """
        super().__init__()
        self.login(user, password)
        transfer_link = self.driver.find_element(
            By.XPATH, Transfer_Locators.TRANSFER_LINK_LOCATOR)
        transfer_link.click()
        transfer_bet_accounts = self.driver.find_element(
            By.XPATH, Transfer_Locators.TRANSFER_BET_ACCOUNTS_LOCATOR)
        transfer_bet_accounts.click()

    def select_a_user(self, user):
        """
        method to select a user
        user str: user to be selected
        return : None
        """
        select_user = Select(self.driver.find_element(
            By.XPATH, Transfer_Locators.SELECT_USER_LOCATOR))
        select_user.select_by_visible_text(user)

    def select_available_debit_account(self, index=0):
        """
        select an available account for debit, default is first
        index int: index at which debit account to be selected
        return : None
        """
        select_debit_acct = Select(self.driver.find_element(
            By.XPATH, Transfer_Locators.ACCOUNT_FROM_LOCATOR))
        select_debit_acct.select_by_index(index)

    def select_available_credit_account(self, index=1):
        """
        method to select a credit account, defaults to index 1 so that it's different from debit account
        index int: index at which credit account to be selected
        return : None
        """
        select_credit_acct = Select(self.driver.find_element(
            By.XPATH, Transfer_Locators.ACCOUNT_TO_LOCATOR))
        select_credit_acct.select_by_index(index)

    def enter_amount_to_transfer(self, amount):
        """
        method to enter amount to be transferred
        amount float: amount to be transferred
        return : None
        """
        enter_amount = self.driver.find_element(
            By.XPATH, Transfer_Locators.AMOUNT_LOCATOR)
        enter_amount.send_keys(amount)

    def enter_description(self, description):
        """
        method to enter description
        description str: description to be added
        return : None
        """
        description = self.driver.find_element(
            By.CSS_SELECTOR, Transfer_Locators.DESCRIPTION_LOCATOR)
        description.send_keys(description)

    def continue_transfer(self):
        """
        method to continue transfer
        return : None
        """
        continue_transfer = self.driver.find_element(
            By.XPATH, Transfer_Locators.CONTINUE_BUTTON_LOCATOR)
        continue_transfer.click()

    def confirm_transfer(self):
        """
        method to confirm
        return : None
        """
        confirm_transfer = self.driver.find_element(
            By.XPATH, Transfer_Locators.CONFIRM_BUTTON_LOCATOR)
        confirm_transfer.click()

    def verify_success(self):
        """
        method to verify that
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, Transfer_Locators.SUCCESS_LOCATOR)))
