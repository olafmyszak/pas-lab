import socket


def handle_request(request, client_socket):
    if request.strip() == 'GET_IMAGE':
        # Implement logic to send the image to the client
        pass
    elif request.strip() == 'GET_LIST':
        # Implement logic to send the list of available files to the client
        pass
    elif request.startswith('GET_FILE '):
        file_name = request.split()[1]
        # Implement logic to send the specified file to the client
        pass
    else:
        client_socket.sendall(b"ERROR \r\n")


def protocol_server_with_file_list():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Protocol server with file list listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        request = client_socket.recv(1024).decode()
        handle_request(request, client_socket)

        client_socket.close()


protocol_server_with_file_list()
