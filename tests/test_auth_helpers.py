def test_auth_helper(session):
    print(session.session_key)
    print(session.check_active_auth())
    print(session.logout())
