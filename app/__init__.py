import os
from kobin import Kobin, TemplateResponse
from . import models, views

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))

models.setup_models(app)
models.setup_redis(app)
views.setup_routing(app)


@app.route('/')
def index():
    return TemplateResponse('index.html')
