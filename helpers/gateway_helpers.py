import data.endpoints as endpoints
import models.http as http


def analitics_info(session):
    resp = http.parametrized_get(host=session['host'], endpoint=endpoints.url['analiticsinfo'],
                                 header_payload={'DeviceToken': session['devicetoken'],
                                                  'SessionToken': session['sessiontoken'],
                                                  'Content-Type': r'application/json'})
    return resp


def deposit_rateinfo(session):
    resp = http.parametrized_get(host=session['host'], endpoint=endpoints.url['depositrateinfo'],
                                 header_payload={'DeviceToken': session['devicetoken'],
                                                  'SessionToken': session['sessiontoken'],
                                                  'Content-Type': r'application/json'})
    return resp
