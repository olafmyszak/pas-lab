import socket

server_address = ("localhost", 2908)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect(server_address)

    message = input("Podaj wiadomość (maksymalnie 20 znaków): ")

    if len(message) < 20:
        message = message.ljust(20)
    elif len(message) > 20:
        message = message[:20]

    total_sent = 0
    while total_sent < len(message):
        sent = sock.send(message[total_sent:].encode())
        total_sent += sent

    response = b''
    expected_len = len(message)
    while len(response) < expected_len:
        chunk = sock.recv(expected_len - len(response))
        response += chunk

    data = sock.recv(1024)

    print(f"Odebrana wiadomość: \"{data.decode()}\". Długość: {len(data.decode())} znaków")


except socket.error as e:
    print(e)

finally:
    sock.close()
