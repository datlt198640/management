FROM nginx:1.19.5-alpine

RUN mkdir /resource
RUN mkdir /resource/ssl
RUN mkdir /resource/public

WORKDIR /resource
