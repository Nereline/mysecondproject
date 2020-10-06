import requests
import data.users


def login_init():

    resp = requests.post('http://testbankok.akbars.ru/AkbarsOnlineAuth/LoginInit',
                  data={'login': data.users.protas['login'], 'password': data.users.protas['password']})

    print(resp.status_code == requests.codes.ok)
    assert resp.status_code == 200, 'Not 200 {}'.format(resp.status_code)

    json = resp.json()
    result = json['Result']
    data.users.session['operationid'] = result['AkbarsLoginOperationId']
    print(data.users.session['operationid'])
    return True


def login_confirm():
    resp = requests.post('http://testbankok.akbars.ru/AkbarsOnlineAuth/LoginConfirm',
                      data={'AkbarsOnlineLoginOperationId': data.users.session['operationid'], 'DeviceToken': data.users.session['devicetoken']})

    json = resp.json()
    result = json['Result']
    data.users.session['refreshtoken'] = result['RefreshToken']
    print(data.users.session['refreshtoken'])
    return True


def set_pin():
    resp = requests.post('http://testbankok.akbars.ru/auth/setPin',
                      data={'RefreshToken': data.users.session['refreshtoken'],
                            'Pin': data.users.protas['pin'],
                            'DeviceToken': data.users.session['devicetoken']})
    return True


def create_session():
    resp = requests.post('http://testbankok.akbars.ru/auth/createsession',
                      data={'RefreshToken': data.users.session['refreshtoken'],
                            'Pin': data.users.protas['pin']})

    json = resp.json()
    result = json['Result']
    data.users.session['sessiontoken'] = result['SessionToken']
    a = (resp.status_code == requests.codes.ok, resp.text)
    print(data.users.session['sessiontoken'])
    print(a)

    return a

