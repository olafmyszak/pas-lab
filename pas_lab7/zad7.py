import socket


def pop3_client_total_bytes(server, port, user, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server, port))
        sock.recv(1024)

        sock.sendall(b"USER " + user.encode() + b"\r\n")
        sock.recv(1024)

        sock.sendall(b"PASS " + password.encode() + b"\r\n")
        sock.recv(1024)

        sock.sendall(b"STAT\r\n")
        response = sock.recv(1024).decode()

        total_bytes = response.split()[2]
        print("Łączna liczba bajtów:", total_bytes)

        sock.sendall(b"QUIT\r\n")
        sock.recv(1024)


pop3_client_total_bytes('interia.pl', 110, 'pas2017@interia.pl', 'P4SInf2017')
