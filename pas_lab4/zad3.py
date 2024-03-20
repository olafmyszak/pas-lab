import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    data, addr = server_socket.recvfrom(4096)
    print('Połączenie nawiązane z', addr)

    server_socket.sendto(data, addr)
