# kobin-example

Example application in Kobin python web-framework.


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

