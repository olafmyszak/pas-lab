import socket
import sys

# print(f"IP address: {sys.argv[1]}")
# print(f"IP is {socket.gethostbyname(sys.argv[1])}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 30)

print("starting up on %s port %s" % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    conn, addr = sock.accept()