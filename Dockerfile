FROM amazonlinux:latest

RUN mkdir -p /opt/pong-srv

COPY pong.py /opt/pong-srv/

RUN ls -lrth /opt/pong-srv/ 

RUN which python3

#CMD ["sh", "-c", "python3 /opt/pong-srv/pong.py"]

#RUN python3 /opt/pong-srv/pong.py


