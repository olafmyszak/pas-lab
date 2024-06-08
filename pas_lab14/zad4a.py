import socket

server_ip = '212.182.24.27'
server_port = 29443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((server_ip, server_port))

    while True:
        message = input("Enter a message to send: ")

        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)

        print("Received:", response.decode())
