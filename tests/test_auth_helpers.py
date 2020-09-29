import helpers.auth_helpers


print('도와주세요')


def test_auth_helper():
    helpers.auth_helpers.simple_auth_check()
    assert helpers.auth_helpers.simple_auth_check(), 'Could not auth =('


