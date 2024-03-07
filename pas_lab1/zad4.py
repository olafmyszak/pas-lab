import socket
import sys

# print(f"IP address: {sys.argv[1]}")
print(f"Hostname is {socket.gethostbyaddr(sys.argv[1])}")