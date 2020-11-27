import requests


def parametrized_get(endpoint=None,
                     url_payload=None,
                     header_payload=None,
                     expected_response_codes=[200],
                     host=None,
                     timeout=60,
                     with_auth=True):
    """
    Get запрос
    :param endpoint: Эндпоинт запроса, подставляется после host
    :param url_payload: Служит для передачи необходимых данных прямо в url запроса
    :param header_payload: Хедеры запроса
    :param expected_response_codes: Ожидаемый массив допустимых кодов ответа, по умолчанию 200
    :param host: Часть url-адреса, склеивается с endpoint
    :param timeout: Допустимое время исполнения запроса, по умолчанию 60
    :param with_auth: Пока не использует. Флаг с типом bool, True - авторизация нужна False - не нужна
    :return:
    """
    if header_payload is None:
        header_payload = {'User-Agent': 'ABOL/3.74.0-test (Android 8.0.0; samsung SM-A520F)'}
    r = requests.get(host+endpoint, params=url_payload,
                     headers=header_payload, timeout=timeout, verify=False)
    assert r.status_code in expected_response_codes, \
        f'Response code not {expected_response_codes}, actually response code {r.status_code}'
    result = r.json()
    return result


def parametrized_post(endpoint=None,
                      url_payload=None,
                      data=None,
                      body_payload=None,
                      files=None,
                      header_payload=None,
                      expected_response_codes=[200],
                      host=None,
                      timeout=60,
                      with_auth=True):
    """
    POST запрос
    :param endpoint: Эндпоинт запроса, подставляется после host
    :param url_payload: Служит для передачи необходимых данных прямо в url запроса
    :param data: Передача тела запроса в формате неформатировнного текста
    :param body_payload: Передача тела запроса в формате json
    :param files: Служит для передачи файла в запросе, если он есть
    :param header_payload: Хедеры запроса
    :param expected_response_codes: Ожидаемый массив допустимых кодов ответа, по умолчанию 200
    :param host: Часть url-адреса, склеивается с endpoint
    :param timeout: Допустимое время исполнения запроса, по умолчанию 60
    :param with_auth: Пока не использует. Флаг с типом bool, True - авторизация нужна False - не нужна
    :return:
    """
    if header_payload is None:
        header_payload = {'User-Agent': 'ABOL/3.74.0-test (Android 8.0.0; samsung SM-A520F)'}
    r = requests.post(host+endpoint, params=url_payload, data=data,
                      headers=header_payload, json=body_payload, timeout=timeout, files=files, verify=False)
    assert r.status_code in expected_response_codes, \
        f'Response code not {expected_response_codes}, actually response code {r.status_code}'
    result = r.json()
    return result
