import socket

server_host = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_host, server_port))

server_socket.listen(5)

print(f"Server listening on {server_host}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        client_socket.sendall(data)

    client_socket.close()
