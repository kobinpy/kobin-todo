import os

ENV = os.getenv('KOBIN_TODO_ENV', 'develop')

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

GITHUB_CLIENT_ID = os.environ.get('KOBIN_TODO_GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.environ.get('KOBIN_TODO_GITHUB_CLIENT_SECRET')

if ENV == 'develop':
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DEBUG = True
elif ENV == 'test':
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = True
elif ENV == 'docker':
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DEBUG = False
