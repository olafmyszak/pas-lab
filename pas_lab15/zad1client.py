import socket

server_host = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_host, server_port))

print(f"Connected to server {server_host}:{server_port}")

try:
    while True:
        message = input("Enter message: ")

        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print("Response:", response.decode())
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client_socket.close()
