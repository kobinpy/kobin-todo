import os
from kobin import Kobin, template

app = Kobin()
app.config.load_from_pyfile(os.environ.get('KOBIN_SETTINGS_FILE', 'config/local.py'))


@app.route('^/$')
def index():
    return template('index')

if __name__ == '__main__':
    app.run()
