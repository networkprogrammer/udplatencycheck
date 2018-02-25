import socket  # for sockets
import sys  # for exit
import datetime, time

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

while (1):
    #msg = raw_input('Enter message to send : ')
    timenow = datetime.datetime.utcnow()
    #print(timenow)
    msg = timenow.strftime("%Y-%m-%d %H:%M:%S.%f")
    try:
        # Set the whole string
        s.sendto(msg, (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        timenow = datetime.datetime.utcnow()
        reply = d[0]
        addr = d[1]
        sentdatetime = datetime.datetime.strptime(reply.split(',')[1], "%Y-%m-%d %H:%M:%S.%f")
        #print("Client Reported Time :" + timenow.strftime("%Y-%m-%d %H:%M:%S.%f"))
        #print("Server Reported Time : " + sentdatetime.strftime("%Y-%m-%d %H:%M:%S.%f"))
        diff = timenow - sentdatetime
        print('forwardlatency=' + reply.split(',')[0] +",reverselatency=" + str(diff.total_seconds()*1000))
        time.sleep(2)
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()