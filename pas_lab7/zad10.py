import socket


def pop3_client_all_messages(server, port, user, password):
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
            sock.sendall(f"RETR {message_id}\r\n".encode())
            message_content = sock.recv(4096).decode()
            print(f"Treść wiadomości {message_id}:\n", message_content)

        sock.sendall(b"QUIT\r\n")
        sock.recv(1024)


pop3_client_all_messages('interia.pl', 110, 'pas2017@interia.pl', 'P4SInf2017')
