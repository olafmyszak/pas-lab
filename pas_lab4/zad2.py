import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(1)

while True:
    client_socket, addr = server_socket.accept()
    print('Połączenie nawiązane z', addr)

    data = client_socket.recv(4096)

    client_socket.sendall(data)

    client_socket.close()
