FROM python:3.6-rc-slim
MAINTAINER Masashi Shibata <contact@c-bata.link>

RUN apt-get update && apt-get install -y --no-install-recommends git gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
ADD requirements /usr/src/requirements
RUN pip install \
    -c /usr/src/requirements/constraints.txt \
    -r /usr/src/requirements/docker.txt

ADD ./app /usr/src/app
ADD ./templates /usr/src/templates
ADD ./manage.py /usr/src/manage.py

WORKDIR /usr/src
EXPOSE 80
CMD ["gunicorn", "-w", "1", "-b", ":80", "app:app"]
