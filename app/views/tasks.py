from kobin import response, request, HTTPError
import json

from .. import models
from ..service import task as task_service


def task_list():
    response.add_header('Content-Type', 'application/json')
    tasks = [t.serialize for t in models.session.query(models.Task).all()]
    return json.dumps({'tasks': tasks})


def add_task():
    response.add_header('Content-Type', 'application/json')
    new_task = task_service.add_task(title=request.json['title'])
    return json.dumps(new_task.serialize)


def get_task(task_id: int):
    response.add_header('Content-Type', 'application/json')
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPError(404, "Not found: {}".format(repr(request.path)))
    return json.dumps(task.serialize)


def update_task(task_id: int):
    response.add_header('Content-Type', 'application/json')
    updated_task = task_service.update_task(task_id, request.json['task'])
    return json.dumps(updated_task.serialize)


def delete_task(task_id: int):
    if not task_service.delete_task(task_id):
        raise HTTPError(404, "Task is not found.")
    response.status = 204
    return ''
