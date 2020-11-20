import data.endpoints as endpoints
import models.http as http
import requests
import bs4
import re
from datetime import timedelta, datetime


def login_init(session):
    """
    Инициализация авторизации пользователя, приходит флаг для понимания, нужен ли ввод отп
    В теле передаёт логин и пароль пользователя
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['loginInit'],
                                  body_payload={'login': session['testuser']['login'],
                                                'password': session['testuser']['password']})

    session['operationid'] = resp['Result']['AkbarsLoginOperationId']
    session['needotp'] = resp['Result']['NeedOtp']
    if session['needotp'] is True:
        send_otp(session)
        get_otp(session)
    return resp


def login_confirm(session):
    """
    Подтверждение
    В теле запроса передаётся operationid, devicetoken и otp если нужно
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['loginConfirm'],
                                  body_payload={'AkbarsOnlineLoginOperationId': session['operationid'],
                                        'DeviceToken': session['devicetoken'], 'otpCode': session['otp']})

    session['refreshtoken'] = resp['Result']['RefreshToken']
    return resp


def set_pin(session):
    """
    Функция для установки пин-кода "девайса"
    В теле запроса передаётся refreshtoken, devicetoken, pin
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['setPin'],
                                  body_payload={'RefreshToken': session['refreshtoken'],
                                        'Pin': session['testuser']['pin'],
                                        'DeviceToken': session['devicetoken']})
    return resp


def create_session(session):
    """
    Функция для создания токена сессии
    В теле запроса передаётся refreshtoken и pin
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['createSession'],
                                  body_payload={'RefreshToken': session['refreshtoken'],
                                        'Pin': session['testuser']['pin']})

    session['sessiontoken'] = resp['Result']['SessionToken']
    session['optime'] = datetime.now()
    return resp


def send_otp(session):
    """
    Функция для отправки отп
    Используется, если LoginInit вернул флаг "NeedOtp": true
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['sendOtp'],
                                  body_payload={'AkbarsOnlineLoginOperationId': session['operationid']},
                                  header_payload={'Content-Type': r'application/json; charset=UTF-8'})
    return resp


def get_otp(session):
    """
    Функция для получения отп через апи
    Используется, если LoginInit вернул флаг "NeedOtp": true
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_get(host='http://testbankok.akbars.ru/', endpoint=endpoints.url['zagadki'],
                                 url_payload={"operationToken": "IdentityAbo:" + session['operationid']})
    session['otp'] = resp['code']
    return resp


def get_otp_from_web(session):
    """
    Функция для получения отп через страницу загадок
    Используется, если LoginInit вернул флаг "NeedOtp": true
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает True
    """

    resp = requests.get(session['host'] + endpoints.url['zagadki_web'])
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    data_table = soup.find('td', {'class': 'col-md-8'})
    result = data_table.text
    rez = re.compile(r'\d+')
    session['otp'] = rez.findall(result)
    return True


def logout(session):
    """
    Функция для выхода пользователя из АБО
    Затирает токен сессии
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['logout'],
                                  data='{"SessionToken":"' + session['sessiontoken'] + '"}',
                                  header_payload={'DeviceToken': session['devicetoken'],
                                                  'SessionToken': session['sessiontoken'],
                                                  'Content-Type': r'application/json'})
    session['sessiontoken'] = ''
    return resp


def remove_push_token(session):
    """
    Функция для выхода пользователя из АБО
    Делает пуш токен невалидным, наверное
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_post(host=session['host'], endpoint=endpoints.url['removePushToken'],
                                  data='{"PushToken":"' + session['pushtoken'] +
                                       '","DeviceToken":"' + session['devicetoken'] + '"}',
                                  header_payload={'Content-Type': r'application/json'})
    return resp


class Session:
    """
    Класс Session принимает на вход тестового юзера. Используется для хранения атрибутов сесси пользователя.
    Основное применения - логин, логаут, проверка сессии на протухание.

    Атрибуты:
    last_auth_time - время последней авторизации
    session_key - токен сессии
    test_user - тестовый юзер, которого класс получает на входе
    session - словарь, содержайший основные параметры сессии пользователя

    Методы:
    create_session - метод создания сессии
    logout - метод для логаута
    check_active_auth - метод проверки "свежести" сессии пользователя
    """

    def __init__(self, test_user):
        self.last_auth_time = None
        self.session_key = None
        self.test_user = test_user
        self.session = {
            'devicetoken': '18FCA794-4243-4AF2-8001-9F27CD8376FE',
            'operationid': '',
            'refreshtoken': '',
            'sessiontoken': '',
            'optime': '',
            'pushtoken': 'bf4f062733ed1ab3e9a0df5a5f058366320ce7bfd1dcf3a11e543f404788165a',
            'otp': '',
            'needotp': '',
            'testuser': test_user,
            'host': 'http://testbankok.akbars.ru/'
        }

    def create_session(self):
        """
        Метод для создания сессии
        :return:
        Возвращает токен сессии
        """

        login_init(self.session)
        login_confirm(self.session)
        set_pin(self.session)
        create_session(self.session)
        self.last_auth_time = self.session['optime']
        self.session_key = self.session['sessiontoken']
        return self.session_key

    def logout(self):
        """
        Метод для логаута. Затирает значение токена сессии
        :return:
        Возвращает токен сессии (пустой)
        """

        logout(self.session)
        remove_push_token(self.session)
        self.session_key = None
        return self.session_key

    def check_active_auth(self):
        """
        Метод для проверки сесии на время истечения
        Если времени после создания сессии прошло больше, чем 2,5 минут, создастся новая сессия
        :return:
        Возвращает Тру
        """

        if self.session_key is not None and self.last_auth_time is not None:
            session_rec_time = timedelta(minutes=2, seconds=30)
            now = datetime.now()
            time_after_login = now - self.last_auth_time
            if time_after_login > session_rec_time:
                self.create_session()
        return True
    pass
