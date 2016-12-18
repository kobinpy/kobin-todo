from kobin import request, RedirectResponse, current_config
from datetime import timedelta

from .. import app
from ..service import github as github_service


def github_oauth_callback():
    code = request.query['code']
    payload = {
        "client_id": app.config.get('GITHUB_CLIENT_ID'),
        "client_secret": app.config.get('GITHUB_CLIENT_SECRET'),
        "code": code,
    }
    access_token = github_service.get_access_token(payload)
    user_info = github_service.get_github_user_info(access_token)
    user = github_service.get_or_create_user(
        nickname=user_info['login'],
        name=user_info['name'],
        avatar_url=user_info['avatar_url'],
        auth_service='github',
        auth_service_id=user_info['id'],
        email=user_info['email'],
    )

    r = app.config.get('REDIS')
    r.set('access_token_{id}'.format(id=user.id), access_token)
    response = RedirectResponse(app.router.reverse('top'))
    response.set_cookie("user_id", f"access_token_{user.id}",
                        max_age=timedelta(days=1), path='/',
                        secret=current_config()['SECRET_KEY'])
    return response


def logout():
    response = RedirectResponse(app.router.reverse('top'))
    response.delete_cookie('user_id')
    return response
