from . import models


def add_task(title: str=None) -> models.Task:
    new_task = models.Task(title=title)
    models.session.add(new_task)
    models.session.commit()
    return new_task
