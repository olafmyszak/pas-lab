import random
import socket


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


server_address = ("127.0.0.1", 2912)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(server_address)
    sock.listen(1)

    has_guessed = False

    while not has_guessed:
        conn, addr = sock.accept()
        random_num = random.randint(-100, 100)

        while not has_guessed:
            try:
                data = conn.recv(1024).decode()

                if not is_number(data):
                    conn.sendall("Blad: to nie jest liczba".encode())
                else:
                    guess = float(data)

                    if guess == random_num:
                        conn.sendall("Zgadles".encode())
                        has_guessed = True

                    elif guess > random_num:
                        conn.sendall("Za duzo".encode())
                    else:
                        conn.sendall("Za malo".encode())

            except socket.error as e:
                print(e)
                break

        conn.close()
