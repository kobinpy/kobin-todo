import os
import redis
from kobin import Kobin, template
from . import models, views

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))

app.config['redis'] = redis.StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
)
views.setup_routing(app)


@app.route('^/$')
def index():
    return template('index')
