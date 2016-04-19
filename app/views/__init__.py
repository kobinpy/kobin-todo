def setup_routing(app):
    from . import tasks
    from . import auth

    # tasks
    app.route('^/api/tasks$', 'GET', tasks.task_list)
    app.route('^/api/tasks$', 'POST', tasks.add_task)
    app.route('^/api/tasks/(?P<task_id>\d+)$', 'GET', tasks.add_task)
    app.route('^/api/tasks/(?P<task_id>\d+)$', 'PATCH', tasks.update_task)
    app.route('^/api/tasks/(?P<task_id>\d+)$', 'DELETE', tasks.delete_task)

    # auth
    app.route('^/auth/github/callback$', 'GET', auth.github_oauth_callback)
