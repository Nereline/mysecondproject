import helpers.auth_helpers
import data.users


def test_auth_helper():
    session = {
        'devicetoken': '18FCA794-4243-4AF2-8001-9F27CD8376FE',
        'operationid': '',
        'refreshtoken': '',
        'sessiontoken': '',
        'otp': '',
        'needotp': '',
        'testuser': data.users.protas,
        'host': 'http://testbankok.akbars.ru/'
    }

    helpers.auth_helpers.login_init(session)
    if session['needotp'] is True:
        helpers.auth_helpers.send_otp(session)
        helpers.auth_helpers.get_otp(session)
        helpers.auth_helpers.login_confirm(session)
        helpers.auth_helpers.set_pin(session)
        helpers.auth_helpers.create_session(session)
    else:
        helpers.auth_helpers.login_confirm(session)
        helpers.auth_helpers.set_pin(session)
        helpers.auth_helpers.create_session(session)
