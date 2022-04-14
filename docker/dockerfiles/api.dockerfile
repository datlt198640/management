FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

ADD ./requirements.txt /app/


RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
            gcc \
            libc-dev \ 
            linux-headers \ 
            postgresql-dev  \
            musl-dev \
            zlib \
            zlib-dev

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r ./requirements.txt

RUN apk del .tmp-build-deps
