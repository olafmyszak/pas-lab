import socket


def handle_client_connection(client_socket):
    client_socket.sendall(b"220 Welcome to Fake SMTP Server\r\n")

    while True:
        data = client_socket.recv(1024).decode().strip()
        if data:
            print(f"Received: {data}")
            if data.upper().startswith("EHLO") or data.upper().startswith("HELO"):
                client_socket.sendall(
                    b"250-Hello\r\n250-SIZE 35882577\r\n250-8BITMIME\r\n250-PIPELINING\r\n250-STARTTLS\r\n250 OK\r\n")
            elif data.upper().startswith("MAIL FROM:"):
                client_socket.sendall(b"250 OK\r\n")
            elif data.upper().startswith("RCPT TO:"):
                client_socket.sendall(b"250 OK\r\n")
            elif data.upper().startswith("DATA"):
                client_socket.sendall(b"354 End data with <CR><LF>.<CR><LF>\r\n")
            elif data == ".":
                client_socket.sendall(b"250 OK: queued as 12345\r\n")
            elif data.upper().startswith("QUIT"):
                client_socket.sendall(b"221 Bye\r\n")
                break
            else:
                client_socket.sendall(b"502 Command not implemented\r\n")


def smtp_server():
    bind_ip = '127.0.0.1'
    bind_port = 1025

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((bind_ip, bind_port))
    server_socket.listen(5)

    print(f"Server listening on {bind_ip}:{bind_port}")

    while True:
        client_sock, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        handle_client_connection(client_sock)
        client_sock.close()


smtp_server()
