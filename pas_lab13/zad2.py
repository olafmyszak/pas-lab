import socket


def send_file(file_name, server_socket):
    with open(file_name, 'rb') as file:
        server_socket.sendall(f"{file_name},{len(file.read())}".encode())
        file.seek(0)
        while True:
            data = file.read(1024)
            if not data:
                break
            server_socket.sendall(data)


def upload_client(file_name):
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to server {host}:{port}")

    send_file(file_name, client_socket)

    print("File sent successfully")

    client_socket.close()


upload_client('example.jpg')
