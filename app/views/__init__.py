def setup_routing(app):
    from kobin import TemplateResponse, request, HTTPError
    from . import tasks
    from . import auth

    # tasks
    app.route('/api/tasks', 'GET', 'task-list', tasks.task_list)
    app.route('/api/tasks', 'POST', 'task-create', tasks.create_task)
    app.route('/api/tasks/{task_id}', 'GET', 'task-detail', tasks.get_task)
    app.route('/api/tasks/{task_id}', 'PATCH', 'task-task-update', tasks.update_task)
    app.route('/api/tasks/{task_id}', 'DELETE', 'task-delete', tasks.delete_task)

    # auth
    app.route('/auth/github/callback', 'GET', 'github-callback', auth.github_oauth_callback)
    app.route('/logout', 'GET', '/', auth.logout)

    @app.route('/', method='GET', name='top')
    def index():
        if request.environ.get('kobin.user'):
            return TemplateResponse('index.html')
        return TemplateResponse('login.html')

    @app.before_request
    def before():
        redis_access_token_key = request.get_cookie("user_id", default=None,
                                                    secret=app.config['SECRET_KEY'])
        request.environ['kobin.user'] = redis_access_token_key

    @app.after_request
    def after(response):
        if isinstance(response, HTTPError):
            s = app.config['DB']['SESSION']
            s.rollback()
        return response
