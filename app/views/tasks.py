from kobin import request, Response, JSONResponse, HTTPError

from .. import app, models
from ..service import task as task_service


def task_list():
    session = app.config["DB"]["SESSION"]
    tasks = [t.serialize for t in session.query(models.Task).all()]
    return JSONResponse({'tasks': tasks})


def add_task():
    new_task = task_service.add_task(title=request.json['title'])
    return JSONResponse(new_task.serialize)


def get_task(task_id: int):
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPError(f"Not found: {repr(request.path)}", 404)
    return JSONResponse(task.serialize)


def update_task(task_id: int):
    updated_task = task_service.update_task(task_id, request.json['task'])
    return JSONResponse(updated_task.serialize)


def delete_task(task_id: int):
    if not task_service.delete_task(task_id):
        raise HTTPError("Task is not found.", 404)
    return Response('', status=204)
