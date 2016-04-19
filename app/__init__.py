import os
import json
import redis
from kobin import Kobin, template, response, request, HTTPError, redirect
from . import models
from .service import task as task_service

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))

app.config['redis'] = redis.StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
)


@app.route('^/$')
def index():
    return template('index')


@app.route('^/api/tasks$')
def task_list():
    response.add_header('Content-Type', 'application/json')
    tasks = [t.serialize for t in models.session.query(models.Task).all()]
    return json.dumps({'tasks': tasks})


@app.route('^/api/tasks$', method='POST')
def add_task():
    response.add_header('Content-Type', 'application/json')
    new_task = task_service.add_task(title=request.json['title'])
    return json.dumps(new_task.serialize)


@app.route('^/api/tasks/(?P<task_id>\d+)$')
def get_task(task_id: int):
    response.add_header('Content-Type', 'application/json')
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPError(404, "Not found: {}".format(repr(request.path)))
    return json.dumps(task.serialize)


@app.route('^/api/tasks/(?P<task_id>\d+)$', method='PATCH')
def update_task(task_id: int):
    response.add_header('Content-Type', 'application/json')
    updated_task = task_service.update_task(task_id, request.json['task'])
    return json.dumps(updated_task.serialize)


@app.route('^/api/tasks/(?P<task_id>\d+)$', method='DELETE')
def delete_task(task_id: int):
    if not task_service.delete_task(task_id):
        raise HTTPError(404, "Task is not found.")
    response.status = 204
    return ''


@app.route('^/auth/github/callback$')
def github_oauth_callback():
    code = request.GET['code'].value
    from .service import github
    payload = {
        "client_id": app.config.get('GITHUB_CLIENT_ID'),
        "client_secret": app.config.get('GITHUB_CLIENT_SECRET'),
        "code": code,
    }
    access_token = github.get_access_token(payload)
    user = github.get_user(access_token)

    r = app.config['redis']
    r.set('access_token_{id}'.format(id=user["id"]), access_token)
    return redirect('/')
