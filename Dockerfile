FROM amazonlinux:latest

RUN mkdir -p /opt/pong-srv

WORKDIR /opt/pong-srv/

COPY pong.py /opt/pong-srv/

CMD ["python", "pong.py"]


