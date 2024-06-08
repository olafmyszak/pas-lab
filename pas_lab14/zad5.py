import socket
import ssl


def echo_server():
    host = '127.0.0.1'
    port = 12345

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('server.pem')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        ssl_server_socket = context.wrap_socket(server_socket, server_side=True)

        ssl_server_socket.bind((host, port))

        ssl_server_socket.listen(5)

        print(f"Echo server listening on {host}:{port}")

        while True:
            client_socket, client_address = ssl_server_socket.accept()
            print(f"Connection from {client_address}")

            data = client_socket.recv(1024)

            client_socket.sendall(data)

            client_socket.close()


echo_server()
