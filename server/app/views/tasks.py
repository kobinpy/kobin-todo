from kobin import request, Response, JSONResponse, HTTPError

from ..service import task as task_service


def task_list():
    tasks = [t.serialize for t in task_service.retrieve_tasks()]
    return JSONResponse({'tasks': tasks})


def create_task():
    new_task = task_service.create_task(title=request.json['title'])
    return JSONResponse(new_task.serialize)


def get_task(task_id: int):
    task = task_service.retrieve_task(task_id)
    if task is None:
        raise HTTPError(f"Not found: {request.path}", 404)
    return JSONResponse(task.serialize)


def update_task(task_id: int):
    updated_task = task_service.update_task(task_id, request.json['task'])
    return JSONResponse(updated_task.serialize)


def delete_task(task_id: int):
    if not task_service.delete_task(task_id):
        raise HTTPError("Task is not found.", 404)
    return Response('', status=204)
