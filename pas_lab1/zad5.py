import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 30)

print("starting up on %s port %s" % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    conn, addr = sock.accept()
