import requests


def parametrized_get(endpoint=None,
                     url_payload=None,
                     header_payload=None,
                     expected_response_codes=[200],
                     host=None,
                     timeout=60):
    if header_payload is None:
        header_payload = {'User-Agent': 'ABOL/3.74.0-test (Android 8.0.0; samsung SM-A520F)'}
        r = requests.get(host+endpoint, params=url_payload,
                         headers=header_payload, timeout=timeout)
        assert r.status_code in expected_response_codes, \
            f'Response code not {expected_response_codes}, actually response code {r.status_code}'
        result = r.json()
    return result


def parametrized_post(endpoint=None,
                      url_payload=None,
                      data=None,
                      body_payload=None, #чо-т не поняла, для чего нужно
                      files=None,
                      header_payload=None,
                      expected_response_codes=[200],
                      host=None,
                      timeout=60):
    if header_payload is None:
        header_payload = {'User-Agent': 'ABOL/3.74.0-test (Android 8.0.0; samsung SM-A520F)'}
    r = requests.post(host+endpoint, params=url_payload, data=data,
                      headers=header_payload, timeout=timeout, files=files)
    assert r.status_code == 200 in expected_response_codes, \
        f'Response code not {expected_response_codes}, actually response code {r.status_code}'
    result = r.json()
    return result
