import base64
import hashlib
import socket
import struct


def websocket_server():
    host = "127.0.0.1"
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"WebSocket server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024)
        if data:
            headers = data.decode().split("\r\n")
            key = None
            for header in headers:
                if "Sec-WebSocket-Key" in header:
                    key = header.split(": ")[1]
                    break
            if key:
                accept_key = base64.b64encode(
                    hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest())
                response = (
                    "HTTP/1.1 101 Switching Protocols\r\n"
                    "Upgrade: websocket\r\n"
                    "Connection: Upgrade\r\n"
                    f"Sec-WebSocket-Accept: {accept_key.decode()}\r\n\r\n"
                )
                client_socket.send(response.encode())

                while True:
                    data = client_socket.recv(1024)
                    if data:
                        payload_length = data[1] & 127
                        if payload_length == 126:
                            payload_length = struct.unpack(">H", data[2:4])[0]
                            mask_start = 4
                        elif payload_length == 127:
                            payload_length = struct.unpack(">Q", data[2:10])[0]
                            mask_start = 10
                        else:
                            mask_start = 2

                        mask = data[mask_start:mask_start + 4]
                        encrypted_payload = data[mask_start + 4:]
                        payload = bytearray([encrypted_payload[i] ^ mask[i % 4] for i in range(len(encrypted_payload))])

                        print(f"Received message: {payload.decode()}")

                        response_header = b"\x81"
                        if payload_length <= 125:
                            response_header += struct.pack("B", payload_length)
                        elif payload_length <= 65535:
                            response_header += struct.pack("!BH", 126, payload_length)
                        else:
                            response_header += struct.pack("!BQ", 127, payload_length)
                        client_socket.send(response_header + payload)

        client_socket.close()


websocket_server()
