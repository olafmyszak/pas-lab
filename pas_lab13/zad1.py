import socket


def receive_file(file_name, client_socket):
    with open(file_name, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)


def upload_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Upload server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive file name and file size
        file_info = client_socket.recv(1024).decode()
        file_name, file_size = file_info.split(',')
        file_size = int(file_size)

        print(f"Receiving file {file_name} ({file_size} bytes)")

        # Receive and save the file
        receive_file(file_name, client_socket)

        print("File received successfully")

        client_socket.close()


upload_server()
