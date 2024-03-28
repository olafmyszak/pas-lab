import socket

server_address = ("212.182.24.27", 2912)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(3)

    try:
        sock.connect(server_address)

        while True:
            try:
                print("Podaj liczbe: ", end='')
                guess = input()
                sock.sendall(guess.encode())
                print(sock.recv(1024).decode())

            except socket.error as e:
                print(e)
                break

    except socket.error as e:
        print(e)
