from kobin import Kobin, template
import config

app = Kobin()
app.config.load_from_module(config)


@app.route('^/$')
def index():
    return template('index')

if __name__ == '__main__':
    app.run()
