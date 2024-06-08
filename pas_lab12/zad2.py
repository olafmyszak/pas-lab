import socket
from datetime import datetime


def echo_server_with_logging():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    log_file = open("server_log.txt", "a")

    print(f"Echo server with logging listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        log_file.write(f"{datetime.now()} - Connection from {client_address}\n")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.send(data)

        client_socket.close()


echo_server_with_logging()
