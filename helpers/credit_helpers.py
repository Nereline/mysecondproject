import data.endpoints as endpoints
import models.http as http


class CreditV3:
    def __init__(self, session):
        self.session = session

    @staticmethod
    def test_credits_params(session):
        resp = http.parametrized_post(host=session['host'],
                                      endpoint=endpoints.url['creditapplications_parameters_v3'],
                                      header_payload={'SessionToken': session['sessiontoken'],
                                                      'Content-Type': r'application/json; charset=UTF-8'})
        return resp
