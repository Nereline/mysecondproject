import pytest
import helpers.credit_helpers as credit_helpers
from conftest import test_credit_user, default_user
from helpers.auth_helpers import Session
import data.endpoints as endpoints
import models.http as http


class TestCredit:

    @pytest.fixture(scope="class")
    def test_session(self, test_credit_user):
        class_session = Session(test_credit_user)
        class_session.create_session()
        return class_session.session

    def test_get_credits_params(self, test_session):
        resp = credit_helpers.CreditV3.test_credits_params(test_session)
        assert resp['Success'] is True, f"Запрос не успешен. " \
                                        f"Фактический результа выполнения запроса {resp['Success']}"

    def test_2(self, test_session):
        """Для пробы, чтобы увидеть, что у меня 2 теста запускаются, а потом отрабатывает тирдаун"""
        resp = http.parametrized_get(host=test_session['host'], endpoint=endpoints.url['analiticsinfo'],
                                     header_payload={'DeviceToken': test_session['devicetoken'],
                                                     'SessionToken': test_session['sessiontoken'],
                                                     'Content-Type': r'application/json'})
        return resp

    @classmethod
    def teardown_class(cls):
        user = default_user
        class_session = Session(user)
        class_session.create_session()
