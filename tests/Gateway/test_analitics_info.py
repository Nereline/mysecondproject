import helpers.gateway_helpers as gateway_helpers


def test_analitics_info(session):
    gateway_helpers.analitics_info(session.session)
