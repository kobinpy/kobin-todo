import requests
import json
from typing import Dict
from kobin import request, HTTPError

from .. import app, models


def get_or_create_user(nickname: str, name: str, auth_service: str, avatar_url: str,
                       auth_service_id: int, email: str) -> models.User:
    session = app.config["SESSION"]
    user = session.query(models.User).filter_by(
        auth_service=auth_service, auth_service_id=auth_service_id
    ).first()

    if user is None:
        user = models.User(
            nickname=nickname,
            name=name,
            avatar_url=avatar_url,
            auth_service=auth_service,
            auth_service_id=auth_service_id,
            email=email,
        )
    session.add(user)
    session.commit()
    return user


def current_user() -> models.User:
    user_id = int(request.environ['kobin.user'].split('_')[-1])
    session = app.config["SESSION"]
    return session.query(models.User).get(user_id)


def get_github_user_info(access_token: str) -> Dict:
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
