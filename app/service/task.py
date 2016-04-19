from app import models
from typing import Dict, Any


def add_task(title: str=None) -> models.Task:
    new_task = models.Task(title=title)
    models.session.add(new_task)
    models.session.commit()
    return new_task


def get_task(task_id) -> models.Task:
    return models.session.query(models.Task).get(task_id)


def update_task(task_id: int, new_task: Dict[str, Any]) -> models.Task:
    task = get_task(task_id)
    task.update(**new_task)
    models.session.add(task)
    models.session.commit()
    return task


def delete_task(task_id: int) -> bool:
    task = get_task(task_id)
    if task is None:
        return False
    models.session.delete(task)
    models.session.commit()
    return True
