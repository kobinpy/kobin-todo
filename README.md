# kobin-example

Example application in Kobin python web-framework.

![animation](./anim.gif)

## Running Kobin TODO by Docker

Set Environment Variables.

```sh
export KOBIN_TODO_GITHUB_CLIENT_ID=xxxxxxxxxxxxxxxxxxxx
export KOBIN_TODO_GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Run with Docker.

```console
$ docker-compose build
$ docker-compose up -d
$ docker-compose run server python manage.py migrate
```

Other:

- bash: `docker-compose exec server /bin/bash`
- logs: `docker-compose logs server`
- psql: `psql -h localhost --user kobin kobintodo`


## How to build

Set Environment Variables

```sh
export KOBIN_TODO_ENV=develop
export KOBIN_TODO_GITHUB_CLIENT_ID=xxxxxxxxxxxxxxxxxxxx
export KOBIN_TODO_GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Compile TypeScript and Stylus

```console
$ cd front
$ npm install
$ npm run build
```

Setup python interpreter

```console
$ python3.6 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

Run redis and postgresql

```console
$ docker-compose up -d redis postgres
```

Run

```
$ python manage.py run
```
