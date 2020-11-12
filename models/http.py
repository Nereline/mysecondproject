import requests
from helpers.auth_helpers import Session


def parametrized_get(session=Session,
                     endpoint=None,
                     url_payload=None,
                     header_payload=None,
                     expected_response_codes=[200],
                     host=None,
                     timeout=60):
    if header_payload is None:
        header_payload = {'User-Agent': 'ABOL/3.74.0-test (Android 8.0.0; samsung SM-A520F)'}
    if session.session_key is None:
        pass
    else:
        session.check_active_auth()
    r = requests.get(host+endpoint, params=url_payload,
                     headers=header_payload, timeout=timeout, verify=False)
    assert r.status_code in expected_response_codes, \
        f'Response code not {expected_response_codes}, actually response code {r.status_code}'
    result = r.json()
    return result


def parametrized_post(session=Session,
                      endpoint=None,
                      url_payload=None,
                      data=None,
                      body_payload=None,  #чо-т не поняла, для чего нужно body_payload
                      files=None,
                      header_payload=None,
                      expected_response_codes=[200],
                      host=None,
                      timeout=60):
    if header_payload is None:
        header_payload = {'User-Agent': 'ABOL/3.74.0-test (Android 8.0.0; samsung SM-A520F)'}
    if session.session_key is None:
        pass
    else:
        session.check_active_auth()
    r = requests.post(host+endpoint, params=url_payload, data=data,
                      headers=header_payload, timeout=timeout, files=files, verify=False)
    assert r.status_code in expected_response_codes, \
        f'Response code not {expected_response_codes}, actually response code {r.status_code}'
    result = r.json()
    return result
