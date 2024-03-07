import socket
from concurrent.futures import ThreadPoolExecutor


def test_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)

        try:
            sock.connect((host, port))
            return socket.getservbyport(port)
        except:
            return False


def port_scan(host, ports):
    with ThreadPoolExecutor(len(ports)) as executor:
        results = executor.map(test_port, [host] * len(ports), ports)

        for port, result in zip(ports, results):
            if result is not False:
                print(f'{port} is open')
                print(f'usluga: {result}')


HOST = 'localhost'

i = 0
j = 10000
MAX = 65535

while i < MAX and j < MAX:
    PORTS = range(i, j)
    port_scan(HOST, PORTS)
    i = j
    j += 10000

