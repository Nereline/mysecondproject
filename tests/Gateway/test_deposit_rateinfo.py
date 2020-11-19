import helpers.gateway_helpers as gateway_helpers


def test_analitics_info(session):
    print(gateway_helpers.deposit_rateinfo(session.session))
