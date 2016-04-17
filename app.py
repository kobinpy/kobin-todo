import os
import json
from kobin import Kobin, template, response

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))


@app.route('^/$')
def index():
    return template('index')


@app.route('^/api/tasks$')
def task_list():
    response.add_header('Content-type', 'application/json')
    tasks = [
        {
            "id": 1,
            "message": "task 1",
            "done": False,
        },
        {
            "id": 2,
            "message": "task 2",
            "done": True,
        },
        {
            "id": 3,
            "message": "task 3",
            "done": False,
        },
        {
            "id": 4,
            "message": "task 4",
            "done": False,
        },
    ]
    return json.dumps({'tasks': tasks})

if __name__ == '__main__':
    app.run()
