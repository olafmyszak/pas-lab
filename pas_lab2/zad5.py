import socket

server_address = ("localhost", 2901)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    sock.connect(server_address)

    while True:
        text = input()
        sock.sendall(text.encode())

        data = sock.recv(4096)
        print(f"Odebrano: {data.decode()}")

except socket.error:
    print("Socket error")
