import socket

server_address = ('localhost', 2906)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(server_address)

while True:
    data, client_address = server_socket.recvfrom(4096)
    ip_address = data.decode()

    hostname = socket.gethostbyaddr(ip_address)[0]

    server_socket.sendto(hostname.encode(), client_address)
    print("Wysłano nazwę hosta", hostname, "do", client_address)
