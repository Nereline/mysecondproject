import pytest
from helpers.auth_helpers import Session


@pytest.fixture(scope="session")
def session(test_user):
    """
    Фикстура служащая для создания сессии пользователя
    :param test_user: На вход принимает тестового юзера из фикстуры test_user
    :return: Возвращается объект типа Session
    """
    session = Session(test_user)
    session.create_session()
    return session
