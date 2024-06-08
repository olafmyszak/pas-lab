import socket
import ssl

server_ip = '212.182.24.27'
server_port = 29443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    ssl_client_socket = ssl.wrap_socket(client_socket)

    ssl_client_socket.connect((server_ip, server_port))

    while True:
        message = input("Enter a message to send: ")

        ssl_client_socket.sendall(message.encode())

        response = ssl_client_socket.recv(1024)

        print("Received:", response.decode())
