import socket

server_address = ('localhost', 2907)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

print("Serwer UDP nasłuchuje na porcie", server_address[1])

try:
    while True:
        data, client_address = server_socket.recvfrom(1024)
        hostname = data.decode()
        ip_address = socket.gethostbyname(hostname)
        server_socket.sendto(ip_address.encode(), client_address)
        print("Wysłano adres IP", ip_address, "do", client_address)
except Exception as e:
    print("Wystąpił błąd:", e)
finally:
    server_socket.close()
