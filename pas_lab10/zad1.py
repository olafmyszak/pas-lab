import socket


def websocket_client_handshake():
    host = "echo.websocket.org"
    port = 80

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    handshake = (
        "GET / HTTP/1.1\r\n"
        "Host: echo.websocket.org\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
        "Sec-WebSocket-Version: 13\r\n\r\n"
    )
    client_socket.send(handshake.encode())

    response = client_socket.recv(1024)
    print(response.decode())

    client_socket.close()


websocket_client_handshake()
