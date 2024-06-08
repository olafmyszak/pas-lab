import socket
import ssl

host = '127.0.0.1'
port = 12345

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='client.pem', keyfile='client.key')

with socket.create_connection((host, port)) as client_socket:
    ssl_client_socket = context.wrap_socket(client_socket, server_hostname=host)

    while True:
        message = input("Enter a message to send: ")

        ssl_client_socket.sendall(message.encode())

        response = ssl_client_socket.recv(1024)

        print("Received:", response.decode())
