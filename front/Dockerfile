FROM node:7.3

RUN mkdir -p /usr/src/public
WORKDIR /usr/src

ADD ./package.json /usr/src/package.json
ADD ./yarn.lock /usr/src/yarn.lock

RUN npm install -g yarn && \
    npm install

ADD ./img /usr/src/img
ADD ./stylus /usr/src/stylus
ADD ./ts /usr/src/ts
ADD ./tsconfig.json /usr/src/tsconfig.json

RUN npm run build

# Shared folder should enable after npm build.
VOLUME /usr/src/public
