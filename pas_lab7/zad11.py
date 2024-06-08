import base64
import email
import socket


def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)


def pop3_client_download_attachment(server, port, user, password):
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

            email_message = email.message_from_string(message_content)
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                if filename:
                    with open(filename, 'wb') as f:
                        f.write(decode_base64(part.get_payload()))
                    print(f"Pobrano załącznik: {filename}")

        sock.sendall(b"QUIT\r\n")
        sock.recv(1024)


pop3_client_download_attachment('interia.pl', 110, 'pas2017@interia.pl', 'P4SInf2017')
