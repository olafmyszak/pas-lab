import socket
import datetime

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(1)


while True:
    client_socket, addr = server_socket.accept()
    print('Połączenie nawiązane z', addr)

    client_socket.recv(1024)

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    client_socket.sendall(current_datetime.encode())

    client_socket.close()
