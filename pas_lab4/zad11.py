import re
import socket


def use_regex(input_text, pattern):
    pattern = re.compile(pattern, re.IGNORECASE)
    return pattern.match(input_text)


server_address = ("127.0.0.1", 2911)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(server_address)
    messageA_correct = False

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
            data = data.decode()
            print(data)

            if not messageA_correct:
                if use_regex(data, "zad15odpA;ver;[0-9]+;srcip;[0-9]+;dstip;[0-9]+;type;[0-9]+"):
                    if data == "zad15odpA;ver;4;srcip;3568703515;dstip;3232235522;type;6":
                        sock.sendto("TAK".encode(), client_address)
                        messageA_correct = True
                    else:
                        sock.sendto("NIE".encode(), client_address)

                else:
                    sock.sendto("BAD_SYNTAX".encode(), client_address)

            elif messageA_correct:
                messageA_correct = False
                if use_regex(data, "zad15odpB;srcport;[0-9]+;dstport;[0-9]+;data;[0-9]+"):
                    if data == ("zad15odpB;srcport;2900;dstport;47526;data;15617344897515034349418636211077958225135483"
                                "338141217080373756523057991302338616653166"):
                        sock.sendto("TAK".encode(), client_address)
                    else:
                        sock.sendto("NIE".encode(), client_address)
                else:
                    sock.sendto("BAD_SYNTAX".encode(), client_address)

        except socket.error as e:
            print(e)
            break
