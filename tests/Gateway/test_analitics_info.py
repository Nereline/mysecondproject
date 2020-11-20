import helpers.gateway_helpers as gateway_helpers


def test_analitics_info(session):
    resp = gateway_helpers.analitics_info(session.session)
    assert resp['Success'] is True, f"Запрос не успешен. Фактический результ выполнения запроса {resp['Success']}"
    assert resp['Result']['Identifier'] is not None, f"Отсутствует CRM id пользователя"
