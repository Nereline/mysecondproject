import data.endpoints as endpoints
import models.http as http


def analitics_info(session):
    """
    Функция для получения СРМ ид и флагов зарплатника/сотрудника/випа пользователя
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_get(host=session['host'], endpoint=endpoints.url['analiticsinfo'],
                                 header_payload={'DeviceToken': session['devicetoken'],
                                                  'SessionToken': session['sessiontoken'],
                                                  'Content-Type': r'application/json'})
    # assert resp['Success'] is True, f'Success is not True'
    return resp


def deposit_rateinfo(session):
    """
    Функция для получения максимальной процентной ставки по депозиту
    :param session:
    На вход принимает словарик с атрибутами сессии пользователя
    :return:
    Возвращает тело респонса
    """

    resp = http.parametrized_get(host=session['host'], endpoint=endpoints.url['depositrateinfo'],
                                 header_payload={'DeviceToken': session['devicetoken'],
                                                  'SessionToken': session['sessiontoken'],
                                                  'Content-Type': r'application/json'})
    # assert resp['Success'] is True, f'Success is not True'
    return resp
