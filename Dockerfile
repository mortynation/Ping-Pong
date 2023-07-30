FROM amazonlinux:latest

LABEL maintainer="Nivaas"
LABEL description="Pong Service Image"
LABEL version="1.0"

RUN mkdir -p /opt/pong-srv

WORKDIR /opt/pong-srv/

COPY pong.py /opt/pong-srv/

CMD ["python3", "pong.py"]


