import data.endpoints
import models.http


def login_init(session):

    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['loginInit'],
                                         data={'login': session['testuser']['login'],
                                               'password': session['testuser']['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    session['needotp'] = resp['Result']['NeedOtp']
    return resp


def login_confirm(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['loginConfirm'],
                                         data={'AkbarsOnlineLoginOperationId': session['operationid'],
                                               'DeviceToken': session['devicetoken'], 'otpCode': session['otp']})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    return resp


def set_pin(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['setPin'],
                                         data={'RefreshToken': session['refreshtoken'],
                                               'Pin': session['testuser']['pin'],
                                               'DeviceToken': session['devicetoken']})
    return resp


def create_session(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['createSession'],
                                         data={'RefreshToken': session['refreshtoken'],
                                               'Pin': session['testuser']['pin']})

    session['sessiontoken'] = resp['Result']['SessionToken']
    return resp


def send_otp(session):
    resp = models.http.parametrized_post(host=session['host'], endpoint=data.endpoints.url['sendOtp'],
                                         data='{"AkbarsOnlineLoginOperationId":"'+session['operationid']+'"}',
                                         header_payload={'Content-Type': r'application/json; charset=UTF-8'})
    return resp


def get_otp(session):
    resp = models.http.parametrized_get(host='http://testbankok.akbars.ru/', endpoint=data.endpoints.url['zagadki'],
                                        url_payload={"operationToken": "IdentityAbo:" + session['operationid']})
    session['otp'] = resp['code']
    return resp
