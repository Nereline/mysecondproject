import requests
import data.users
import models.http


def login_init(session):

    resp = models.http.parametrized_post(endpoint='AkbarsOnlineAuth/LoginInit',
                                    data={'login': data.users.protas['login'], 'password': data.users.protas['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    return True


def login_confirm(session):
    resp = models.http.parametrized_post(endpoint='AkbarsOnlineAuth/LoginConfirm',
                                         data={'AkbarsOnlineLoginOperationId': session['operationid'],
                                               'DeviceToken': session['devicetoken']})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    return True


def set_pin(session):
    resp = models.http.parametrized_post(endpoint='auth/setPin',
                                         data={'RefreshToken': session['refreshtoken'],
                                               'Pin': data.users.protas['pin'],
                                               'DeviceToken': session['devicetoken']})
    return True


def create_session(session):
    resp = models.http.parametrized_post(endpoint='auth/createsession',
                                         data={'RefreshToken': session['refreshtoken'],
                                               'Pin': data.users.protas['pin']})

    session['sessiontoken'] = resp['Result']['SessionToken']
    return resp

