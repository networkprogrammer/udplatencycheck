FROM alpine
RUN apk add --update python
EXPOSE 8888/udp
COPY udpserver.py /var/tmp/udpserver.py
RUN chmod +x /var/tmp/udpserver.py
ENTRYPOINT python /var/tmp/udpserver.py