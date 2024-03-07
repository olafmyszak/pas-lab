import socket

server_address = ('localhost', 2907)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    hostname = "google.com"
    client_socket.sendto(hostname.encode(), server_address)
    ip_address, _ = client_socket.recvfrom(1024)
    print("Odpowiedź od serwera:", ip_address.decode())
except Exception as e:
    print("Wystąpił błąd:", e)
finally:
    client_socket.close()
