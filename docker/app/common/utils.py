import json

import requests
from requests.exceptions import HTTPError

from app.common.config import API_URL, PARAM_COUNT


def get_questions(questions_number: int):
    try:
        resp = requests.get(API_URL, params={PARAM_COUNT: questions_number})
        resp.raise_for_status()
        resp_list = json.loads(resp.content.decode('utf-8'))
        return resp_list
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
