def setup_routing(app):
    from . import tasks
    from . import auth

    # tasks
    app.route('/api/tasks', 'GET', 'task-list', tasks.task_list)
    app.route('/api/tasks', 'POST', 'task-create', tasks.add_task)
    app.route('/api/tasks/{task_id}', 'GET', 'task-detail', tasks.add_task)
    app.route('/api/tasks/{task_id}', 'PATCH', 'task-task-update', tasks.update_task)
    app.route('/api/tasks/{task_id}', 'DELETE', 'task-delete', tasks.delete_task)

    # auth
    app.route('/auth/github/callback', 'GET', 'github-callback', auth.github_oauth_callback)
