import socket
import struct
import time

addr = "ntp.task.gda.pl"
port = 123

REF_TIME_1970 = 2208988800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'\x1b' + 47 * b'\0'
client.sendto(data, (addr, port))

data, address = client.recvfrom(1024)
t = None
if data:
    t = struct.unpack('!12I', data)[10]
    t -= REF_TIME_1970

print(time.ctime(t))

