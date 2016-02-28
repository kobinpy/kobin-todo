FROM centos
MAINTAINER Masashi Shibata <contact@c-bata.link>

# RUN: buildする時に実行される
RUN echo "now building..."

# CMD: runする時に実行される
CMD ["echo", "now running..."]

