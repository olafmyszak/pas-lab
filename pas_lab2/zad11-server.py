import socket

server_address = ('localhost', 2908)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    server_socket.bind(server_address)
    server_socket.listen(1)

    while True:
        connection_socket, client_address = server_socket.accept()

        message = connection_socket.recv(1024).decode()

        if len(message) < 20:
            message = message.ljust(20)
        elif len(message) > 20:
            message = message[:20]

        connection_socket.send(message.encode())

        connection_socket.close()
except Exception as e:
    print("Wystąpił błąd:", e)
finally:
    server_socket.close()
