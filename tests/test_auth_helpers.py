import helpers.auth_helpers as auth_helpers
import data.users as users


def test_auth_helper():
    session = {
        'devicetoken': '18FCA794-4243-4AF2-8001-9F27CD8376FE',
        'operationid': '',
        'refreshtoken': '',
        'sessiontoken': '',
        'otp': '',
        'needotp': '',
        'testuser': users.reimond,
        'host': 'http://testbankok.akbars.ru/'
    }

    auth_helpers.login_init(session)
    if session['needotp'] is True:
        auth_helpers.send_otp(session)
        auth_helpers.get_otp(session)

    auth_helpers.login_confirm(session)
    auth_helpers.set_pin(session)
    auth_helpers.create_session(session)
