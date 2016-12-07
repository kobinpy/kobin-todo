import click
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
    subprocess.call(['wsgicli', 'run', 'app/__init__.py', 'app',
                     '-p', '8080', '--reload',
                     '--static', '--static-root', '/static/',
                     '--static-dirs', './public/static/'])


@cli.command()
def shell():
    """Run shell"""
    subprocess.call(['wsgicli', 'shell', 'app', '-i', 'ipython'])


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
