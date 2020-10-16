import requests


def parametrized_get(endpoint=None,
                     url_payload=None,
                     header_payload=None,
                     expected_response_codes=200,
                     host='http://testbankok.akbars.ru/',
                     timeout=60):
    if header_payload is None:
        header_payload = {'UserAgent': 'python-requests/2.21.0'}
        r = requests.get(host+endpoint,
                         params=url_payload, timeout=timeout)
        assert r.status_code == 200 in expected_response_codes, \
            'Response code not 200, actually response code {}'.format(r.status_code)
        result = r.json()
    pass


def parametrized_post(endpoint=None,
                      url_payload=None,
                      data=None,
                      body_payload=None, #чо-т не поняла, для чего нужно
                      files=None,
                      header_payload=None,
                      expected_response_codes=[200],
                      host='http://testbankok.akbars.ru/',
                      timeout=60):
    if header_payload is None:
        header_payload = {'UserAgent': 'python-requests/2.21.0'}
    r = requests.post(host+endpoint, data=data,
                      params=url_payload, headers=header_payload, timeout=timeout, files=files)
    assert r.status_code == 200 in expected_response_codes, \
        f'Response code not 200, actually response code {r.status_code}'
    result = r.json()
    return result

