import socket
import re


def use_regex(input_text):
    pattern = re.compile(r"zad13odp;src;[0-9]+;dst;[0-9]+;data;[0-9]+", re.IGNORECASE)
    return pattern.match(input_text)


server_address = ("127.0.0.1", 2910)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        try:
            sock.bind(server_address)
            data, client_address = sock.recvfrom(1024)
            data = data.decode()

            if use_regex(data):
                if data == "zad13odp;src;2900;dst;35211;data;700304775037748134333740928275063771249193":
                    sock.sendto("TAK".encode(), client_address)
                else:
                    sock.sendto("NIE".encode(), client_address)
            else:
                sock.sendto("BAD_SYNTAX".encode(), client_address)

        except socket.error as e:
            print(e)
            break
