import socket


def hex_to_dec(hex_str):
    return int(hex_str, 16)


def extract_ipv4_packet_info(hex_packet):
    version = hex_to_dec(hex_packet[0]) >> 4
    src_ip = '.'.join(str(hex_to_dec(hex_packet[i:i + 2])) for i in range(12, 16))
    dst_ip = '.'.join(str(hex_to_dec(hex_packet[i:i + 2])) for i in range(16, 20))
    protocol = hex_to_dec(hex_packet[9])

    if protocol == 6:
        src_port = hex_to_dec(hex_packet[20:24])
        dst_port = hex_to_dec(hex_packet[24:28])
        data_length = hex_to_dec(hex_packet[28:32]) - 20
    elif protocol == 17:
        src_port = hex_to_dec(hex_packet[20:24])
        dst_port = hex_to_dec(hex_packet[24:28])
        data_length = hex_to_dec(hex_packet[28:32]) - 8
    else:
        return None

    return version, src_ip, dst_ip, protocol, src_port, dst_port, data_length


def send_udp_message(message):
    UDP_IP = "212.182.24.27"
    UDP_PORT = 2911
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
        data, _ = sock.recvfrom(1024)
    return data.decode()


hex_packet = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"
ipv4_info = extract_ipv4_packet_info(hex_packet)

if ipv4_info:
    ver, src_ip, dst_ip, protocol, src_port, dst_port, data_len = ipv4_info
    message_a = f"zad15odpA;{ver};{src_ip};{dst_ip};{protocol}"
    response_a = send_udp_message(message_a)
    print("Odpowiedź A:", response_a)

    if response_a == "TAK":
        message_b = f"zad15odpB;{src_port};{dst_port};{data_len}"
        response_b = send_udp_message(message_b)
        print("Odpowiedź B:", response_b)
    else:
        print("Odpowiedź A nie jest poprawna.")
else:
    print("Niepoprawny pakiet IPv4.")

