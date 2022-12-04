import pytest

import logger

log = logger.Logger(__name__).logger


@pytest.mark.login
class TestLogin:

    @pytest.mark.positive
    def test_login_valid_credentials(self, login_instance):
        user = (pytest.config['USER']).replace("\n", "")
        password = (pytest.config['PASSWORD']).replace("\n", "")
        log.info("TEST - login with valid credentials started")
        login_instance.enter_username(user)
        log.info("entered username")
        login_instance.enter_password(password)
        log.info("entered password")
        login_instance.click_sign_in_button()
        log.info("clicked sign in button")
        assert login_instance.verify_login_successful()
        log.info("user logged in successfully")
        log.info("TEST - login with valid credentials ended")

    @pytest.mark.negative
    def test_login_invalid_credentials(self, login_instance):
        log.info("TEST - login with invalid credentials started")
        login_instance.enter_username("invalid-user")
        login_instance.enter_password("invalid-pass")
        log.info("entered invalid credentials")
        login_instance.click_sign_in_button()
        log.info("clicked sign in button")
        assert login_instance.verify_graceful_error()
        log.info("asserted graceful error")
        log.info("TEST - login with invalid credentials ended")
