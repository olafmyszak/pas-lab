import socket
import threading


def client_thread(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)

    client_socket.close()


def echo_multithreaded_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Echo multithreaded server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=client_thread, args=(client_socket, client_address))
        client_thread.start()


echo_multithreaded_server()
