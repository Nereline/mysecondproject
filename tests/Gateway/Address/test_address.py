import helpers.address_helpers as address_helpers


def test_find_address(session):
    resp = address_helpers.AddressFind.test_find_address(session.session)
    assert resp['Success'] is True, f"Запрос не успешен. Фактический результат выполнения запроса {resp['Success']}"
