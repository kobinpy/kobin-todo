from coreapi.codecs import JSONCodec
from kobin import request, Response, JSONResponse, HTTPError
from kobin.environs import accept_best_match
from openapi_codec import OpenAPICodec

from ..coreapi_docs import tasks as task_coreapi
from ..service import task as task_service

json_codec = JSONCodec()
openapi_codec = OpenAPICodec()
mimetypes = json_codec.get_media_types() + \
            openapi_codec.get_media_types()


def task_list():
    mimetype = accept_best_match(request.headers['ACCEPT'], mimetypes)
    tasks_document = task_coreapi.tasks_document()
    if mimetype in openapi_codec.get_media_types():
        content = openapi_codec.encode(tasks_document)
        response = Response(content)
    else:
        tasks = [t.serialize for t in task_service.retrieve_tasks()]
        response = JSONResponse({'tasks': tasks})
        mimetype = 'application/json'
    response.headers.add_header('Content-Type', mimetype)
    return response


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
