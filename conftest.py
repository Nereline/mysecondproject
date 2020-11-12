import pytest
from fixtures.auth_fixture import session
import data.users as users


@pytest.fixture
def test_user():
    user = users.reimond
    return user
