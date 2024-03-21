import socket


def extract_tcp_data(datagram):
    src_port = int(datagram[0:4], 16)
    dst_port = int(datagram[4:8], 16)
    data = int(datagram[44:], 16)
    return src_port, dst_port, data


def extract_udp_data(datagram):
    src_port = int(datagram[0:4], 16)
    dst_port = int(datagram[4:8], 16)
    data = int(datagram[16:], 16)
    return src_port, dst_port, data


def extract_ipv4_packet_info(hex_packet):
    version = int(hex_packet[0], 16)
    protocol = int(hex_packet[18:20], 16)
    src_ip = int(hex_packet[24:32], 16)
    dst_ip = int(hex_packet[32:40], 16)

    if protocol == 6:
        src_port, dst_port, data = extract_tcp_data(hex_packet[40:])
    elif protocol == 17:
        src_port, dst_port, data = extract_udp_data(hex_packet[40:])
    else:
        return None

    return version, src_ip, dst_ip, protocol, src_port, dst_port, data


def send_udp_message(message):
    ip = "127.0.0.1"
    port = 2911
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.sendto(message.encode(), (ip, port))
            data, _ = sock.recvfrom(1024)
        except socket.error as e:
            return e

    return data.decode()


hex_packet = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"
ipv4_info = extract_ipv4_packet_info(hex_packet)

if ipv4_info:
    ver, src_ip, dst_ip, protocol, src_port, dst_port, data = ipv4_info
    message_a = f"zad15odpA;ver;{ver};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"
    response_a = send_udp_message(message_a)
    print("Odpowiedź A:", response_a)

    if response_a == "TAK":
        message_b = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"
        response_b = send_udp_message(message_b)
        print("Odpowiedź B:", response_b)
    else:
        print("Odpowiedź A nie jest poprawna.")
else:
    print("Niepoprawny pakiet IPv4.")
