# kobin-example

Example application in Kobin python web-framework.

![animation](./anim.gif)


## How to run

Compile TypeScript and SCSS

```console
$ mkdir -p public/static/js
$ npm install
$ npm run build
```

Setup python interpreter

```console
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

Start running Redis

```console
$ docker-compose up -d
```

Set Environment Variables

```sh
export KOBIN_TODO_ENV=develop
export KOBIN_TODO_GITHUB_CLIENT_ID=xxxxxxxxxxxxxxxxxxxx
export KOBIN_TODO_GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Run

```
$ python manage.py run
```


## Docker

Build a js and a css.

```console
$ mkdir -p public/static/js
$ npm install
$ npm run build
```
Set Environment Variables.

```sh
export KOBIN_TODO_GITHUB_CLIENT_ID=xxxxxxxxxxxxxxxxxxxx
export KOBIN_TODO_GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Run with Docker.

```console
$ docker-compose build
$ docker-compose up -d
$ docker-compose run web python manage.py migrate
```

Other:

- bash: `docker-compose exec web /bin/bash`
- logs: `docker-compose logs web`
