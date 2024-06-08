import random
import socket


def number_guessing_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Number guessing server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        number_to_guess = random.randint(1, 100)
        print(f"Number to guess: {number_to_guess}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            try:
                guess = int(data.decode())
                if guess < number_to_guess:
                    client_socket.send(b"Too low")
                elif guess > number_to_guess:
                    client_socket.send(b"Too high")
                else:
                    client_socket.send(b"Congratulations! You guessed the number.")
                    break
            except ValueError:
                client_socket.send(b"Please enter a number")

        client_socket.close()


number_guessing_server()
