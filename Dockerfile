FROM amazonlinux:latest

LABEL maintainer="Nivaas"
LABEL description="Pong Service Image"
LABEL version="1.0"

RUN mkdir -p $WORKSPACE/pong-srv

WORKDIR $WORKSPACE/pong-srv

COPY pong.py $WORKSPACE/pong-srv

