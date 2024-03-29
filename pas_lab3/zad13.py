import socket


def extract_udp_data(datagram):
    src_port = int(datagram[0:4], 16)
    dst_port = int(datagram[4:8], 16)
    data = int(datagram[16:], 16)
    return src_port, dst_port, data


hex_datagram = ("ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 "
                "75 6e")
hex_datagram = hex_datagram.replace(' ', '')

src_port, dst_port, data = extract_udp_data(hex_datagram)
message = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}".encode()

server_address = ('212.182.24.27', 2910)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

try:
    sock.sendto(message, server_address)
    data, _ = sock.recvfrom(1024)
    print(data.decode())
except socket.error as e:
    print(e)
