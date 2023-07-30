FROM amazonlinux:latest

RUN mkdir -p /opt/pong-srv

COPY pong.py /opt/pong-srv/

RUN ls -lrth /opt/pong-srv/ 

CMD ["python3", "/opt/pong-srv/pong.py"]


