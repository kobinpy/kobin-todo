FROM python:3.6-rc-slim
MAINTAINER Masashi Shibata <contact@c-bata.link>

RUN apt-get update && apt-get install -y --no-install-recommends git gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
ADD requirements /app/requirements
RUN pip install -c /app/requirements/constraints.txt -r /app/requirements/docker.txt

ADD ./app /app/app
ADD ./templates /app/templates
ADD ./public /app/public
ADD ./manage.py /app/manage.py
ADD ./gunicorn_entrypoint.py /app/gunicorn_entrypoint.py

WORKDIR /app
EXPOSE 80
CMD ["gunicorn", "-w", "1", "-b", ":80", "gunicorn_entrypoint:app"]
