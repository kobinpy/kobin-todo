FROM python:3.5-slim
MAINTAINER Masashi Shibata <contact@c-bata.link>

ADD . /code
WORKDIR /code
RUN pip install --upgrade pip setuptools
RUN pip install -c ./requirements/constraints.txt -r ./requirements/general.txt

EXPOSE 8080
ENV KOBIN_SETTINGS_FILE=config/docker.py
CMD ["python", "./app.py"]
