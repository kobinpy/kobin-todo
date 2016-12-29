from coreapi import Document, Link, Field

from ..service import task as task_service


def tasks_document():
    """ Return the top level Document object, containing all the task instances. """
    return Document(
        url='/api/tasks/',
        title='Tasks',
        content={
            'tasks': [task_document(task.id) for task in task_service.retrieve_tasks()],
            'create_task': Link(action='post', fields=[
                Field(name='title', required=True)
            ])
        }
    )


def task_document(identifier):
    """ Return a Document object for a single task instance. """
    task = task_service.retrieve_task(identifier)
    return Document(
        url=f'/api/tasks/{task.id}',
        title='Task',
        content=task.serialize
    )

