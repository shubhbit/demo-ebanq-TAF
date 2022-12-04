from app.transfer_locators import Transfer_Locators
from app.login import Login
from common.utility import wait_for_element_load, wait


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

        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.TRANSFER_LINK_LOCATOR):
            transfer_link = self.driver.find_element(
                *Transfer_Locators.TRANSFER_LINK_LOCATOR)
            wait(1)
            transfer_link.click()

        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.TRANSFER_LINK_LOCATOR))

        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.TRANSFER_BET_ACCOUNTS_LOCATOR):
            transfer_bet_accounts = self.driver.find_element(
                *Transfer_Locators.TRANSFER_BET_ACCOUNTS_LOCATOR)
            transfer_bet_accounts.click()
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.TRANSFER_BET_ACCOUNTS_LOCATOR))

    def select_a_user(self, user):
        """
        method to select a user
        user str: user to be selected
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.SELECT_USER_LOCATOR):
            combo_box = self.driver.find_element(
                *Transfer_Locators.SELECT_USER_LOCATOR)
            combo_box.click()
            wait(1)
            self.driver.find_element(
                Transfer_Locators.USER_OPTION_LOCATOR[0], Transfer_Locators.USER_OPTION_LOCATOR[1].format(user)).click()
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.SELECT_USER_LOCATOR))

    def select_available_debit_account(self, index=0):
        """
        select an available account for debit, default is first
        index int: index at which debit account to be selected
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.ACCOUNT_FROM_LOCATOR):
            select_debit_acct = self.driver.find_element(
                *Transfer_Locators.ACCOUNT_FROM_LOCATOR)
            select_debit_acct.click()
            wait(1)
            for indexing, option in enumerate(select_debit_acct.find_elements(*Transfer_Locators.OPTION_LOCATOR)):
                if index == indexing:
                    option.click()
                    break
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.ACCOUNT_FROM_LOCATOR))

    def select_available_credit_account(self, index=1):
        """
        method to select a credit account, defaults to index 1 so that it's different from debit account
        index int: index at which credit account to be selected
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.ACCOUNT_TO_LOCATOR):
            select_credit_acct = self.driver.find_element(
                *Transfer_Locators.ACCOUNT_TO_LOCATOR)
            select_credit_acct.click()
            wait(1)
            for indexing, option in enumerate(select_credit_acct.find_elements(*Transfer_Locators.OPTION_LOCATOR)):
                if index == indexing:
                    option.click()
                    break
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.ACCOUNT_TO_LOCATOR))

    def enter_amount_to_transfer(self, amount):
        """
        method to enter amount to be transferred
        amount float: amount to be transferred
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.AMOUNT_LOCATOR):
            enter_amount = self.driver.find_element(
                *Transfer_Locators.AMOUNT_LOCATOR)
            enter_amount.send_keys(amount)
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.AMOUNT_LOCATOR))

    def enter_description(self, description):
        """
        method to enter description
        description str: description to be added
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.DESCRIPTION_LOCATOR):
            description_elem = self.driver.find_element(
                *Transfer_Locators.DESCRIPTION_LOCATOR)
            description_elem.send_keys(description)
            wait(1)
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.DESCRIPTION_LOCATOR))

    def continue_transfer(self):
        """
        method to continue transfer
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.CONTINUE_BUTTON_LOCATOR):
            continue_transfer = self.driver.find_element(
                *Transfer_Locators.CONTINUE_BUTTON_LOCATOR)
            continue_transfer.click()
            wait(1)
        else:
            raise Exception("Element: {} not found".format(
                Transfer_Locators.CONTINUE_BUTTON_LOCATOR))

    def confirm_transfer(self):
        """
        method to confirm
        return : None
        """
        if wait_for_element_load(self.driver, self.timeout, Transfer_Locators.CONFIRM_BUTTON_LOCATOR):
            confirm_transfer = self.driver.find_element(
                *Transfer_Locators.CONFIRM_BUTTON_LOCATOR)
            confirm_transfer.click()
            wait(1)

    def verify_success(self):
        """
        method to verify that
        """
        return wait_for_element_load(
            self.driver, self.timeout, Transfer_Locators.SUCCESS_LOCATOR)

    def verify_error_message(self, error):
        """
        method to verify error message
        """
        wait(1)
        return error in self.driver.page_source
