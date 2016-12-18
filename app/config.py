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
    REDIS_PASSWORD = 'password'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kobin:password@localhost/kobintodo'
    DEBUG = True
    SECRET_KEY = b'secretkey'
elif ENV == 'test':
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = 'password'
    REDIS_PASSWORD = None
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = True
    SECRET_KEY = b'secretkey'
elif ENV == 'docker':
    DEBUG = False
    SECRET_KEY = os.environ.get('KOBIN_TODO_SECRET_KEY').encode('utf-8')

    REDIS_HOST = os.environ.get('KOBIN_TODO_REDIS_HOST')
    REDIS_PORT = os.environ.get('KOBIN_TODO_REDIS_PORT')
    REDIS_PASSWORD = os.environ.get('KOBIN_TODO_REDIS_PASSWORD')
    REDIS_DB = os.environ.get('KOBIN_TODO_REDIS_DB')

    host = os.environ.get('KOBIN_TODO_DATABASE_HOST')
    user = os.environ.get('KOBIN_TODO_DATABASE_USER')
    password = os.environ.get('KOBIN_TODO_DATABASE_PASSWORD')
    db = os.environ.get('KOBIN_TODO_DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{db}'
