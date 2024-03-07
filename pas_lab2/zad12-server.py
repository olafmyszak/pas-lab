import socket

server_address = ('localhost', 2908)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(server_address)
    server_socket.listen(1)

    while True:
        connection_socket, client_address = server_socket.accept()

        message = b""
        expected_length = 20
        while len(message) < expected_length:
            chunk = connection_socket.recv(expected_length - len(message))

            message += chunk

        # Wysyłanie potwierdzenia
        total_sent = 0
        while total_sent < len(message):
            sent = connection_socket.send(message[total_sent:])

            total_sent += sent

        print("Odebrana wiadomość:", message.decode())

        connection_socket.close()
except Exception as e:
    print("Wystąpił błąd:", e)
finally:
    server_socket.close()
