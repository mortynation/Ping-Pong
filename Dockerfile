FROM amazonlinux:latest

RUN mkdir -p /opt/pong-srv

COPY pong.py /opt/pong-srv/

RUN chmod 700 /opt/pong-srv/pong.py

RUN ls -lrth /opt/pong-srv/ 

#RUN which python3

#CMD ["/bin/bash", "-c", "/usr/bin/python3 /opt/pong-srv/pong.py"]


#RUN python3 /opt/pong-srv/pong.py

CMD ["/opt/pong-srv/pong.py"]

