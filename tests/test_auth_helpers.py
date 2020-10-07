import helpers.auth_helpers


def test_auth_helper():
    session = {
        'devicetoken': '18FCA794-4243-4AF2-8001-9F27CD8376FE',
        'operationid': '',
        'refreshtoken': '',
        'sessiontoken': ''
    }

    helpers.auth_helpers.login_init(session)
    helpers.auth_helpers.login_confirm(session)
    helpers.auth_helpers.set_pin(session)
    assert helpers.auth_helpers.create_session(session), 'CreateSession failed'




