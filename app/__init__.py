import os
import json
from kobin import Kobin, template, response, request, HTTPError
from . import models, service

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))


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
    new_task = service.add_task(title=request.json['title'])
    return json.dumps(new_task.serialize)


@app.route('^/api/tasks/(?P<task_id>\d+)$')
def get_task(task_id: int):
    response.add_header('Content-Type', 'application/json')
    task = service.get_task(task_id)
    if task is None:
        raise HTTPError(404, "Not found: {}".format(repr(request.path)))
    return json.dumps(task.serialize)


@app.route('^/api/tasks/(?P<task_id>\d+)$', method='PATCH')
def update_task(task_id: int):
    response.add_header('Content-Type', 'application/json')
    updated_task = service.update_task(task_id, request.json['task'])
    return json.dumps(updated_task.serialize)


@app.route('^/api/tasks/(?P<task_id>\d+)$', method='DELETE')
def delete_task(task_id: int):
    if not service.delete_task(task_id):
        raise HTTPError(404, "Task is not found.")
    response.status = 204
    return ''
