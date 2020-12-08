import pytest
from fixtures.auth_fixture import session
import data.users as users


default_user = users.viol
credit_user = users.protas


@pytest.fixture(scope="session")
def test_user():
    """
    Фикстура для задания тестового пользователя
    :return: Возврщается тестового юзера типа dict
    """
    user = default_user
    return user


@pytest.fixture(scope="session")
def test_credit_user():
    """
    Фикстура для задания тестового кредитного пользователя
    :return: Возврщается тестового юзера типа dict
    """
    user = credit_user
    return user
