import helpers.gateway_helpers as gateway_helpers


def test_deposit_rateinfo(session):
    resp = gateway_helpers.deposit_rateinfo(session.session)
    assert resp['Success'] is True, f"Запрос не успешен. Фактический результ выполнения запроса {resp['Success']}"
    assert resp['Result']['MaxPercentageRateText'] == "До 5,75% годовых", \
        "Изменилась процентная ставка по депозиту"
