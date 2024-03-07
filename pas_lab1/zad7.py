import socket
from concurrent.futures import ThreadPoolExecutor


def test_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)

        try:
            sock.connect((host, port))
            return True
        except:
            return False


def port_scan(host, ports):
    with ThreadPoolExecutor(len(ports)) as executor:
        results = executor.map(test_port, [host] * len(ports), ports)

        for port, is_open in zip(ports, results):
            if is_open:
                print(f'{port} is open')


HOST = 'localhost'
PORTS = range(10000)

port_scan(HOST, PORTS)
