import socket

server_address = ("localhost", 2900)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect(server_address)

    while True:
        text = input()
        sock.sendall(text.encode())

        data = sock.recv(1024)
        print(f"Odebrano: {data.decode()}")


except socket.error:
    print("Socket error")
