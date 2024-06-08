import socket

HOST = 'localhost'
PORT = 2910

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.connect((HOST, PORT))

client_socket.sendall(b'zad14odp;src;60788;dst;2901;data;32')

data = client_socket.recv(1024)

print('Otrzymane:', data.decode())
