from app.transfer_locators import Transfer_Locators
from app.login import Login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Transfer(Login):
    def __init__(self):
        super().__init__()
        user = ""
        password = ""
        self.login(user, password)
        transfer_link = self.driver.find_element(
            By.XPATH, Transfer_Locators.TRANSFER_LINK_LOCATOR)
        transfer_link.click()
        transfer_bet_accounts = self.driver.find_element(
            By.XPATH, Transfer_Locators.TRANSFER_BET_ACCOUNTS_LOCATOR)
        transfer_bet_accounts.click()

    def select_a_user(self, user):
        select_user = Select(self.driver.find_element(
            By.XPATH, Transfer_Locators.SELECT_USER_LOCATOR))
        select_user.select_by_visible_text(user)

    def 
