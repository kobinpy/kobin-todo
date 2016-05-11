from config import *

PORT = 8080
HOST = '0.0.0.0'
SERVER = 'gunicorn'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
