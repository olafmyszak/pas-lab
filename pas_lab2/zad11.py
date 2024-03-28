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

    sock.sendall(message.encode())
    data = sock.recv(1024)

    print(f"Odebrana wiadomość: \"{data.decode()}\". Długość: {len(data.decode())} znaków")


except socket.error:
    print("Socket error")

finally:
    sock.close()
