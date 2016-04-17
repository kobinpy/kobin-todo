from . import models
from typing import Dict, Any


def add_task(title: str=None) -> models.Task:
    new_task = models.Task(title=title)
    models.session.add(new_task)
    models.session.commit()
    return new_task


def update_task(task_id: int, new_task: Dict[str, Any]) -> models.Task:
    task = models.session.query(models.Task).get(task_id)
    task.update(**new_task)
    models.session.add(task)
    models.session.commit()
    return task
