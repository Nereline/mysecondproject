import requests
import data.users
import data.endpoints
import models.http


def login_init(session):

    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['loginInit'],
                                    data={'login': data.users.viol['login'], 'password': data.users.viol['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    return True


def login_confirm(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['loginConfirm'],
                                         data={'AkbarsOnlineLoginOperationId': session['operationid'],
                                               'DeviceToken': session['devicetoken'], 'otpCode': ''})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    return True


def set_pin(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['setPin'],
                                         data={'RefreshToken': session['refreshtoken'],
                                               'Pin': data.users.viol['pin'],
                                               'DeviceToken': session['devicetoken']})
    return True


def create_session(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['createSession'],
                                         data={'RefreshToken': session['refreshtoken'],
                                               'Pin': data.users.viol['pin']})

    session['sessiontoken'] = resp['Result']['SessionToken']
    return resp


def sendotp(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['sendOtp'],
                                         data='{"AkbarsOnlineLoginOperationId":"'+session['operationid']+'"}',
                                         header_payload={'Content-Type': r'application/json; charset=UTF-8'})
    return resp


def getotp(session):
    resp = models.http.parametrized_get(host=session['host'], endpoint=data.endpoints.url['zagadki'],
                                        url_payload=session['operationid'])
    return resp

