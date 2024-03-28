import re
import socket


def use_regex(input_text):
    pattern = re.compile(r"zad14odp;src;[0-9]+;dst;[0-9]+;data;[0-9]+", re.IGNORECASE)
    return pattern.match(input_text)


server_address = ('localhost', 2909)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(server_address)

while True:
    data, client_address = server_socket.recvfrom(4096)
    message = data.decode()

    if use_regex(message):
        if message == "zad14odp;src;60788;dst;2901;data;32":
            server_socket.sendto("TAK".encode(), client_address)
        else:
            server_socket.sendto("NIE".encode(), client_address)
    else:
        server_socket.sendto("BAD_SYNTAX".encode(), client_address)
