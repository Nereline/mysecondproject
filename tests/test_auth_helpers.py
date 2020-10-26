import helpers.auth_helpers as auth_helpers
import data.users as users


def test_auth_helper():

    session = auth_helpers.Session(users.reimond)
    print(session.current_user)
    print(session.session_key)
    session.create_session()
    print(session.session_key)
