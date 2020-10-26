import helpers.auth_helpers as auth_helpers
import data.users as users


def test_auth_helper():

    session = auth_helpers.Session(users.reimond)
    print(session.create_session())
