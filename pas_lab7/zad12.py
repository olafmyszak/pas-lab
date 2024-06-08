import socket


def handle_client_connection(client_socket):
    client_socket.sendall(b"+OK POP3 server ready\r\n")

    while True:
        data = client_socket.recv(1024).decode().strip()
        print(f"Received: {data}")

        if data.upper().startswith("USER"):
            client_socket.sendall(b"+OK User accepted\r\n")
        elif data.upper().startswith("PASS"):
            client_socket.sendall(b"+OK Password accepted\r\n")
        elif data.upper().startswith("STAT"):
            client_socket.sendall(b"+OK 2 320\r\n")
        elif data.upper().startswith("LIST"):
            client_socket.sendall(b"+OK 2 messages (320 octets)\r\n1 160\r\n2 160\r\n.\r\n")
        elif data.upper().startswith("RETR"):
            message_id = int(data.split()[1])
            if message_id == 1:
                client_socket.sendall(b"+OK 160 octets\r\nSubject: Test\r\n\r\nThis is a test message.\r\n.\r\n")
            elif message_id == 2:
                client_socket.sendall(
                    b"+OK 160 octets\r\nSubject: Another Test\r\n\r\nThis is another test message.\r\n.\r\n")
        elif data.upper().startswith("QUIT"):
            client_socket.sendall(b"+OK Goodbye\r\n")
            break
        else:
            client_socket.sendall(b"-ERR Command not implemented\r\n")


def pop3_server():
    bind_ip = '127.0.0.1'
    bind_port = 1100

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((bind_ip, bind_port))
    server_socket.listen(1)

    print(f"Server listening on {bind_ip}:{bind_port}")

    while True:
        client_sock, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        handle_client_connection(client_sock)
        client_sock.close()


pop3_server()
