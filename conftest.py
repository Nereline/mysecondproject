import pytest
from fixtures.auth_fixture import session
import data.users as users


@pytest.fixture(scope="session")
def test_user():
    user = users.reimond
    return user
