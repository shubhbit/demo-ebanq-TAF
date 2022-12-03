import pytest

class TestLogin:
    def test_login_valid_credentials(self, login_instance):
        login_instance.enter_username("")
        login_instance.enter_password("")
        login_instance.click_sign_in_button()
        assert login_instance.verify_login_successful()

    def test_login_invalid_credentials(self, login_instance):
        login_instance.enter_username("invalid-user")
        login_instance.enter_password("invalid-pass")
        login_instance.click_sign_in_button()
        assert login_instance.verify_graceful_error()
