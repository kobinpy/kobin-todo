import requests
import json
from typing import Dict
from kobin import HTTPError


def get_user(access_token: str):
    url = "https://api.github.com/user?access_token={token}".format(token=access_token)
    res = requests.get(url)
    return res.json()


def get_access_token(payload: Dict[str, str]):
    headers = {'Content-Type': 'application/json'}
    res = requests.post('https://github.com/login/oauth/access_token',
                        data=json.dumps(payload), headers=headers)
    if res.status_code != 200:
        raise HTTPError("Github authentication error", 500)
    res_params = {k: v for k, v in
                  [p.split('=') for p in res.text.split('&')]}
    return res_params['access_token']
