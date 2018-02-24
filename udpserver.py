import socket
import sys
import datetime

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    timenow = datetime.datetime.utcnow()
    sentdatetime = datetime.datetime.strptime(data,"%Y-%m-%d %H:%M:%S.%f")
    print("Server Reported Time :" + timenow.strftime("%Y-%m-%d %H:%M:%S.%f"))
    print("Client Reported Time : " + sentdatetime.strftime("%Y-%m-%d %H:%M:%S.%f"))
    diff = timenow - sentdatetime
    print("Time Differenece " + str(diff.total_seconds()*1000))
    addr = d[1]

    if not data:
        break
    timenow = datetime.datetime.utcnow()
    reply = str(diff.total_seconds() * 1000) + "," + timenow.strftime("%Y-%m-%d %H:%M:%S.%f")

    s.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

s.close()