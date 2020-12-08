import data.endpoints as endpoints
import models.http as http


class Feed:
    def __init__(self, session):
        self.session = session

    @staticmethod
    def get_feed_v3(session):
        resp = http.parametrized_get(host=session['host'], endpoint=endpoints.url['get_feed_v3'],
                                     header_payload={'DeviceToken': session['devicetoken'],
                                                     'SessionToken': session['sessiontoken'],
                                                     'Content-Type': r'application/json'})
        return resp
