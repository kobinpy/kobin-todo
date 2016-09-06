# kobin-example

Example application in Kobin python web-framework.

![animation](./anim.gif)


## How to run

#### Compile TypeScript and SCSS

```
$ mkdir -p public/static/js
$ npm install
$ npm run build
```

#### Setup python interpreter

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

#### Run

```
$ python manage.py run
```


## Heroku

**NOW, this cannot work in Heroku. Help wanted.**

- https://kobin.herokuapp.com

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

```
$ heroku config:set KOBIN_SETTINGS_FILE=config/heroku.py
```


## Docker

**NOW, this cannot work in Docker. Help wanted.**

```
$ docker build -t c-bata/kobin .
$ docker run -d -p 80:8080 --name kobin c-bata/kobin
```

