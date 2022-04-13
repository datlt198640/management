FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app


RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r ./requirements.txt