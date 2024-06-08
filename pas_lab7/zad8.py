import socket


def pop3_client_each_message_bytes(server, port, user, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server, port))
        sock.recv(1024)

        sock.sendall(b"USER " + user.encode() + b"\r\n")
        sock.recv(1024)

        sock.sendall(b"PASS " + password.encode() + b"\r\n")
        sock.recv(1024)

        sock.sendall(b"LIST\r\n")
        response = sock.recv(1024).decode()

        messages = response.splitlines()[1:-1]
        for message in messages:
            message_id, size = message.split()
            print(f"Wiadomość {message_id}: {size} bajtów")

        sock.sendall(b"QUIT\r\n")
        sock.recv(1024)


pop3_client_each_message_bytes('interia.pl', 110, 'pas2017@interia.pl', 'P4SInf2017')
