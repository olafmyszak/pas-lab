import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], int(sys.argv[2]))

try:
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    print('connected')
except ConnectionRefusedError:
    print('Connection refused!')
