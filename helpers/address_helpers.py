import data.endpoints as endpoints
import models.http as http


class AddressFind:
    def __init__(self, session):
        self.session = session

    @staticmethod
    def test_find_address(session):
        resp = http.parametrized_post(host=session['host'],
                                      endpoint=endpoints.url['find_address'],
                                      body_payload={'SearchTerm': 'г Казань ул Чистопольская 11',
                                                    'MaxCount': 5},
                                      header_payload={'SessionToken': session['sessiontoken'],
                                                      'Content-Type': r'application/json; charset=UTF-8'})
        return resp
