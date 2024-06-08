import base64
import socket
import ssl


def send_command(sock, command):
    sock.sendall(command.encode() + b'\r\n')
    response = sock.recv(1024).decode()
    print(response)
    return response


def smtp_client_with_text_attachment(from_addr, to_addrs, subject, message, attachment_path):
    server = 'interia.pl'
    port = 587
    username = 'pas2017@interia.pl'
    password = 'P4SInf2017'

    with open(attachment_path, 'rb') as file:
        attachment_content = base64.b64encode(file.read()).decode()

    boundary = "sep"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server, port))
        send_command(sock, "EHLO interia.pl")
        send_command(sock, "STARTTLS")

        sock = ssl.wrap_socket(sock)
        send_command(sock, "EHLO interia.pl")

        auth_str = base64.b64encode(f"{username}\0{username}\0{password}".encode()).decode()
        send_command(sock, f"AUTH PLAIN {auth_str}")

        send_command(sock, f"MAIL FROM:<{from_addr}>")
        for addr in to_addrs:
            send_command(sock, f"RCPT TO:<{addr.strip()}>")

        send_command(sock, "DATA")
        message_data = (
            f"Subject: {subject}\r\nTo: {', '.join(to_addrs)}\r\nFrom: {from_addr}\r\n"
            f"MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary={boundary}\r\n\r\n"
            f"--{boundary}\r\nContent-Type: text/plain\r\n\r\n{message}\r\n"
            f"--{boundary}\r\nContent-Type: text/plain; name=\"{attachment_path}\"\r\n"
            f"Content-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{attachment_path}\"\r\n\r\n"
            f"{attachment_content}\r\n--{boundary}--\r\n."
        )
        send_command(sock, message_data)
        send_command(sock, "QUIT")


smtp_client_with_text_attachment('pas2017@interia.pl', ['odbiorca@example.com'], 'Test Email', 'Treść wiadomości.',
                                 'plik.txt')
