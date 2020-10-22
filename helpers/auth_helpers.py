import data.endpoints as endpoints
import models.http as http
import requests
import bs4
import re
import lxml


def login_init(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['loginInit'],
                                  data={'login': session['testuser']['login'],
                                        'password': session['testuser']['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    session['needotp'] = resp['Result']['NeedOtp']
    if session['needotp'] is True:
        send_otp(session)
        get_otp_from_web(session)
    return resp


def login_confirm(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['loginConfirm'],
                                  data={'AkbarsOnlineLoginOperationId': session['operationid'],
                                        'DeviceToken': session['devicetoken'], 'otpCode': session['otp']})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    return resp


def set_pin(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['setPin'],
                                  data={'RefreshToken': session['refreshtoken'],
                                        'Pin': session['testuser']['pin'],
                                        'DeviceToken': session['devicetoken']})
    return resp


def create_session(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['createSession'],
                                  data={'RefreshToken': session['refreshtoken'],
                                        'Pin': session['testuser']['pin']})

    session['sessiontoken'] = resp['Result']['SessionToken']
    return resp


def send_otp(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['sendOtp'],
                                  data='{"AkbarsOnlineLoginOperationId":"' + session['operationid'] + '"}',
                                  header_payload={'Content-Type': r'application/json; charset=UTF-8'})
    return resp


def get_otp(session):
    resp = http.parametrized_get(host='http://testbankok.akbars.ru/', endpoint=endpoints.url['zagadki'],
                                 url_payload={"operationToken": "IdentityAbo:" + session['operationid']})
    session['otp'] = resp['code']
    return resp


def get_otp_from_web(session):
    resp = requests.get(session['host'] + endpoints.url['zagadki_web'])
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    data_table = soup.find('td', {'class': 'col-md-8'})
    result = data_table.text
    rez = re.compile(r'\d+')
    session['otp'] = rez.findall(result)
    return True
