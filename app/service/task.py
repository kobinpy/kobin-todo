from typing import Dict, Any
from .. import app, models


def add_task(title: str=None) -> models.Task:
    new_task = models.Task(title=title)
    session = app.config["DB"]["SESSION"]
    session.add(new_task)
    session.commit()
    return new_task


def get_task(task_id) -> models.Task:
    session = app.config["DB"]["SESSION"]
    return session.query(models.Task).get(task_id)


def update_task(task_id: int, new_task: Dict[str, Any]) -> models.Task:
    task = get_task(task_id)
    task.update(**new_task)
    session = app.config["DB"]["SESSION"]
    session.add(task)
    session.commit()
    return task


def delete_task(task_id: int) -> bool:
    task = get_task(task_id)
    if task is None:
        return False
    session = app.config["DB"]["SESSION"]
    session.delete(task)
    session.commit()
    return True
