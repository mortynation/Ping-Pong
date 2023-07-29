FROM amazonlinux:latest

RUN mkdir -p $WORKSPACE/pong-srv

WORKDIR $WORKSPACE/pong-srv

COPY pong.py $WORKSPACE/pong-srv

