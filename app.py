import os
import json
from kobin import Kobin, template, response, request
import models

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))


@app.route('^/$')
def index():
    return template('index')


@app.route('^/api/tasks$')
def task_list():
    response.add_header('Content-type', 'application/json')
    tasks = [t.serialize() for t in models.session.query(models.Task).all()]
    return json.dumps({'tasks': tasks})


@app.route('^/api/tasks$', method='POST')
def add_task():
    response.add_header('Content-type', 'application/json')
    new_task = models.Task(title=request.POST['title'].value)
    models.session.add(new_task)
    models.session.commit()
    return json.dumps(new_task.serialize)

if __name__ == '__main__':
    app.run()
