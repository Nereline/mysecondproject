import pytest
from fixtures.auth_fixture import session
import data.users as users


@pytest.fixture(scope="session")
def test_user():
    """
    Фикстура для задания тестового пользователя
    :return: Возврщается тестового юзера типа dict
    """
    user = users.reimond
    return user


# @pytest.fixture(scope="test")
# def check_auth(session):
#     session.check_active_auth()
