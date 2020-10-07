import requests
import data.users


def login_init(session):

    resp = requests.post('http://testbankok.akbars.ru/AkbarsOnlineAuth/LoginInit',
                  data={'login': data.users.protas['login'], 'password': data.users.protas['password']})

    assert resp.status_code == 200, 'Not 200 {}'.format(resp.status_code)
    json = resp.json()
    result = json['Result']
    session['operationid'] = result['AkbarsLoginOperationId']
    return True


def login_confirm(session):
    resp = requests.post('http://testbankok.akbars.ru/AkbarsOnlineAuth/LoginConfirm',
                      data={'AkbarsOnlineLoginOperationId': session['operationid'], 'DeviceToken': session['devicetoken']})

    json = resp.json()
    result = json['Result']
    session['refreshtoken'] = result['RefreshToken']
    return True


def set_pin(session):
    resp = requests.post('http://testbankok.akbars.ru/auth/setPin',
                      data={'RefreshToken': session['refreshtoken'],
                            'Pin': data.users.protas['pin'],
                            'DeviceToken': session['devicetoken']})
    return True


def create_session(session):
    resp = requests.post('http://testbankok.akbars.ru/auth/createsession',
                      data={'RefreshToken': session['refreshtoken'],
                            'Pin': data.users.protas['pin']})

    json = resp.json()
    result = json['Result']
    session['sessiontoken'] = result['SessionToken']
    a = (resp.status_code == requests.codes.ok, resp.text)
    return a

