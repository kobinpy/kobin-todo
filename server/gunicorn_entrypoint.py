from app import app
from os import path
from wsgi_static_middleware import StaticMiddleware

# Enable wsgi static middleware
BASE_DIR = path.dirname(path.abspath(__name__))
PUBLIC_DIR = path.join(BASE_DIR, 'public')

app = StaticMiddleware(app, static_root='/static', static_dirs=[PUBLIC_DIR])
