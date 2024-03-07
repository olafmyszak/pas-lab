import socket

server_address = ('localhost', 2906)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    ip_address = "8.8.8.8"
    client_socket.sendto(ip_address.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print("Odpowiedź od serwera:", data.decode())
except Exception as e:
    print("Wystąpił błąd:", e)
finally:
    client_socket.close()
