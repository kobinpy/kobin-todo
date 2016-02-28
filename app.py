from kobin import Kobin, template
import os

app = Kobin()
app.config.update({
    'TEMPLATE_DIRS': [os.path.join(os.path.abspath('.'), 'templates')],
    'STATICFILES_DIRS': [os.path.join(os.path.abspath('.'), 'static')],
    'STATIC_ROOT': '/static/',
})


@app.route('^/$')
def index():
    return template('index')

if __name__ == '__main__':
    app.run()
