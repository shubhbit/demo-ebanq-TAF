import pytest

from app.login import Login
from app.transfer import Transfer


@pytest.fixture(scope="session", autouse=True)
def read_config():
    if not hasattr(pytest, "config"):
        pytest.config = {}
    with open("config.env", "r") as f:
        for line in f:
            line = line.split("=")
            pytest.config[line[0]] = line[1]
    yield
    del pytest.config


@pytest.fixture(scope="function")
def login_instance():
    login_instance = Login()
    yield login_instance
    login_instance.close_driver()
    del login_instance


@pytest.fixture(scope="function")
def transfer():
    user = (pytest.config['USER']).replace("\n", "")
    password = (pytest.config['PASSWORD']).replace("\n", "")
    transfer = Transfer(user, password)
    yield transfer
    transfer.close_driver()
    del transfer
