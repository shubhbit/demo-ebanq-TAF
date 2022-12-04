import pytest
import logger

log = logger.Logger(__name__).logger


@pytest.mark.transfer
class TestTransfer:

    @pytest.mark.positive
    def test_transfer_between_accounts(self, transfer):
        amount = 1
        log.info("TEST - transfer with valid fields started")
        transfer.select_a_user("Mary Johnson (mjohnson)")
        log.info("selected a user")
        transfer.select_available_debit_account()
        log.info("selected debit account")
        transfer.select_available_credit_account()
        log.info("selected credit account")
        transfer.enter_amount_to_transfer(1)
        log.info("entered amount")
        transfer.enter_description(
            'Admin user triggered auto transfer with amount {}'.format(amount))
        log.info("entered description")
        transfer.continue_transfer()
        transfer.confirm_transfer()
        log.info("continue with transaction")
        assert transfer.verify_success()
        log.info("verified success message")
        log.info("TEST - transfer with valid fields ended")

    @pytest.mark.negative
    def test_transfer_between_same_account_graceful_error(self, transfer):
        log.info("TEST - transfer with same account started")
        transfer.select_a_user("Mary Johnson (mjohnson)")
        log.info("selected user")
        transfer.select_available_debit_account()
        transfer.select_available_credit_account(index=0)
        log.info("selected same credit and debit account")
        assert transfer.verify_error_message(
            "Please select different accounts")
        log.info("asserted graceful error message")
        log.info("TEST - transfer with same account ended")

    @pytest.mark.negative
    @pytest.mark.parametrize("amount,error", [("", "Field is required."), (0, "Should be minimum 0.01"), (-1, "Should be minimum 0.01")])
    def test_transfer_invalid_amount(self, transfer, amount, error):
        log.info("TEST - transfer with invalid amount started")
        transfer.select_a_user("Mary Johnson (mjohnson)")
        log.info("selected a user")
        transfer.select_available_debit_account()
        transfer.select_available_credit_account()
        log.info("selected credit and debit accounts")
        transfer.enter_amount_to_transfer(amount)
        log.info("entered invalid amount")
        transfer.continue_transfer()
        assert transfer.verify_error_message(error)
        log.info("verifying graceful error")
        log.info("TEST - transfer with invalid amount ended")
