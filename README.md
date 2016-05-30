# kobin-example

Example application in Kobin python web-framework.

![animation](./anim.gif)


## How to run

```
$ python manage.py --help
Usage: manage.py [OPTIONS] COMMAND [ARGS]...

  This is a management script for the kobin-todo application.

Options:
  --help  Show this message and exit.

Commands:
  lint  Runs code linter.
  run   Runs server.
  test  Runs unit tests.
```


## Heroku

- https://kobin.herokuapp.com

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

```
$ heroku config:set KOBIN_SETTINGS_FILE=config/heroku.py
```


## Docker

```
$ docker build -t c-bata/kobin .
$ docker run -d -p 80:8080 --name kobin c-bata/kobin
```

