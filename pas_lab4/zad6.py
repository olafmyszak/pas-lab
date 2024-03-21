import socket

server_address = ('localhost', 2906)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(server_address)

while True:
    data, client_address = server_socket.recvfrom(4096)
    hostname = data.decode()

    ip_address = socket.gethostbyname(hostname)
    server_socket.sendto(ip_address.encode(), client_address)
