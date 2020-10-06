import helpers.auth_helpers


print('도와주세요')


def test_auth_helper():

    run = helpers.auth_helpers.login_init()
    assert run, 'LoginInit failed =('

    run = helpers.auth_helpers.login_confirm()
    assert run, 'LoginConfirm failed =('

    run = helpers.auth_helpers.set_pin()
    assert run, 'SetPin failed =('

    run = helpers.auth_helpers.create_session()
    assert run, 'CreateSession failed =('




