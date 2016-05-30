import subprocess
import sys
import click

from app import app


@click.group()
def cli():
    pass


@click.command()
def migrate():
    metadata = app.config["DB"].get("METADATA")
    engine = app.config["DB"].get("ENGINE")
    metadata.create_all(engine)


@cli.command()
def run():
    app.run()


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
