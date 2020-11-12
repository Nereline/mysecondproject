import data.endpoints as endpoints
import models.http as http
import requests
import bs4
import re
from datetime import timedelta, datetime


def login_init(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['loginInit'],
                                  data={'login': session['testuser']['login'],
                                        'password': session['testuser']['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    session['needotp'] = resp['Result']['NeedOtp']
    if session['needotp'] is True:
        send_otp(session)
        get_otp(session)
    return resp


def login_confirm(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['loginConfirm'],
                                  data={'AkbarsOnlineLoginOperationId': session['operationid'],
                                        'DeviceToken': session['devicetoken'], 'otpCode': session['otp']})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    # session['pushtoken'] = resp['Result']['IdentityAccessToken']
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
    session['optime'] = datetime.now()
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


def logout(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['logout'],
                                  data='{"SessionToken":"' + session['sessiontoken'] + '"}',
                                  header_payload={'DeviceToken': session['devicetoken'],
                                                  'SessionToken': session['sessiontoken'],
                                                  'Content-Type': r'application/json'})
    session['sessiontoken'] = ''
    return resp


def remove_push_token(session):
    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['removePushToken'],
                                  data='{"PushToken":"' + session['pushtoken'] +
                                       '","DeviceToken":"' + session['devicetoken'] + '"}',
                                  header_payload={'Content-Type': r'application/json'})
    return resp


class Session:

    def __init__(self, current_user):
        self.last_auth_time = None
        self.session_key = None
        self.current_user = current_user
        self.session = {
            'devicetoken': '18FCA794-4243-4AF2-8001-9F27CD8376FE',
            'operationid': '',
            'refreshtoken': '',
            'sessiontoken': '',
            'optime': '',
            'pushtoken': 'bf4f062733ed1ab3e9a0df5a5f058366320ce7bfd1dcf3a11e543f404788165a',
            'otp': '',
            'needotp': '',
            'testuser': current_user,
            'host': 'http://testbankok.akbars.ru/'
        }

    def create_session(self):
        login_init(self.session)
        login_confirm(self.session)
        set_pin(self.session)
        create_session(self.session)
        self.last_auth_time = self.session['optime']
        self.session_key = self.session['sessiontoken']
        return self.session_key

    def logout(self):
        logout(self.session)
        remove_push_token(self.session)
        self.session_key = None
        return self.session_key

    def check_active_auth(self):
        if self.session_key is not None and self.last_auth_time is not None:
            session_rec_time = timedelta(minutes=2, seconds=30)
            now = datetime.now()
            time_after_login = now - self.last_auth_time
            if time_after_login > session_rec_time:
                self.create_session()
        return True
    pass
