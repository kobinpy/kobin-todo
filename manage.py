import click
import os
import subprocess
import sys

from app import app


@click.group()
def cli():
    """This is a management script for the kobin-todo application."""
    pass


@cli.command()
def migrate():
    """Runs database migrations."""
    metadata = app.config["DB"].get("METADATA")
    engine = app.config["DB"].get("ENGINE")
    metadata.create_all(engine)


@cli.command()
def run():
    """Runs server."""
    from wsgiref.simple_server import make_server
    from wsgi_static_middleware import StaticMiddleware
    click.secho('Start: 127.0.0.1:8000', fg='green')
    base_dir = os.path.dirname(os.path.abspath(__name__))
    static_dir = os.path.join(base_dir, 'public/static')
    wrapped_app = StaticMiddleware(app, static_root='/static/', static_dirs=[static_dir])
    httpd = make_server('', 8000, wrapped_app)
    httpd.serve_forever()


@cli.command()
def lint():
    """Runs code linter."""
    lint = subprocess.call(['flake8', '--ignore=E501', 'app/', 'manage.py'])
    if lint:
        print("OK")
    sys.exit(lint)


@cli.command()
def test():
    """Runs unit tests."""
    tests = subprocess.call(['python', '-c', 'import tests; tests.run()'])
    sys.exit(tests)

if __name__ == '__main__':
    cli()
