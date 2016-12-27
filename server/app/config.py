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
    SECRET_KEY = os.environ.get('SECRET_KEY').encode('utf-8')

    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    REDIS_DB = os.environ.get('REDIS_DB')

    host = os.environ.get('POSTGRES_HOST')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    db = os.environ.get('POSTGRES_NAME')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{db}'
