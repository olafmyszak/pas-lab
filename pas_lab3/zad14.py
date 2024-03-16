import socket


def extract_tcp_data(datagram):
    src_port = int(datagram[0:4], 16)
    dst_port = int(datagram[4:8], 16)
    options = int(datagram[44:68], 16)
    data_length = int(len(datagram[68:]) / 2)
    return src_port, dst_port, data_length


datagram = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
datagram = datagram.replace(' ', '')

src_port, dst_port, data_length = extract_tcp_data(datagram)

message = f"zad13odp;src;{src_port};dst;{dst_port};data;{data_length}".encode()
server_address = ('212.182.24.27', 2909)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

try:
    sock.sendto(message, server_address)
    data, _ = sock.recvfrom(1024)
    print(data.decode())

finally:
    sock.close()
