import requests
import data.users


def simple_auth_check():

    resp = requests.post('http://testbankok.akbars.ru/AkbarsOnlineAuth/LoginInit',
                  data={'login': data.users.protas['login'], 'password': data.users.protas['password']})

    #print(resp.text)
    print(resp.status_code == requests.codes.ok)
    assert resp.status_code == 200, 'Not 200 {}'.format(resp.status_code)

    json = resp.json()
    result = json['Result']

    oper_id = result['AkbarsLoginOperationId']
    print(oper_id)

    resp = requests.post('http://testbankok.akbars.ru/AkbarsOnlineAuth/LoginConfirm',
                      data={'AkbarsOnlineLoginOperationId': oper_id, 'DeviceToken': data.users.protas['devicetoken']})
    #print(resp.text)

    json = resp.json()
    result = json['Result']
    refreshtoken = result['RefreshToken']
    print(refreshtoken)

    resp = requests.post('http://testbankok.akbars.ru/auth/createsession',
                      data={'RefreshToken': refreshtoken,
                            'Pin': data.users.protas['pin']})

    resp = requests.post('http://testbankok.akbars.ru/auth/setPin',
                      data={'RefreshToken': refreshtoken,
                            'Pin': data.users.protas['pin'],
                            'DeviceToken': data.users.protas['devicetoken']})
    a = (resp.status_code == requests.codes.ok, resp.text)
    print(a)
    return a

