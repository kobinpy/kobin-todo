from typing import Dict, Any, List
from kobin import HTTPError
from .. import app, models
from ..service import github as github_service


def retrieve_tasks() -> List[models.Task]:
    session = app.config["SESSION"]
    return session.query(models.Task).all()


def create_task(title: str=None) -> models.Task:
    user = github_service.current_user()
    if user is None:
        raise HTTPError(body='You are not logged in.', status=401)

    new_task = models.Task(title=title, user_id=user.id)
    session = app.config["SESSION"]
    session.add(new_task)
    session.commit()
    return new_task


def retrieve_task(task_id) -> models.Task:
    session = app.config["SESSION"]
    return session.query(models.Task).get(task_id)


def update_task(task_id: int, new_task: Dict[str, Any]) -> models.Task:
    task = retrieve_task(task_id)
    task.update(**new_task)
    session = app.config["SESSION"]
    session.add(task)
    session.commit()
    return task


def delete_task(task_id: int) -> bool:
    task = retrieve_task(task_id)
    if task is None:
        return False
    session = app.config["SESSION"]
    session.delete(task)
    session.commit()
    return True
