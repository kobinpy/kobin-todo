from config import *
import os

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
