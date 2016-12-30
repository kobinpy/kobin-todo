import os
from kobin import Kobin, load_config_from_pyfile
from . import views

config = load_config_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'app/config.py'))
app = Kobin(config=config)
views.setup_routing(app)
