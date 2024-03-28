import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
    ADDR = "212.182.24.27"
    TCP_PORT = 2913

    udp_port_list = []
    possible_ports = [666]

    for i in range(1, 65):
        possible_ports.append(i * 1000 + 666)

    while True:
        for port in udp_port_list:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
                udp.sendto("PING".encode(), (ADDR, port))

        tcp.connect((ADDR, TCP_PORT))
        if tcp.recv(1024).decode() == "Congratulations! You found the hidden.":
            break

        tcp.close()

        for port in possible_ports:
            for good_port in udp_port_list:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
                    udp.sendto("PING".encode(), (ADDR, good_port))

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
                udp.sendto("PING".encode(), (ADDR, port))
                data, server = udp.recvfrom(1024)

                if data.decode() == "PONG":
                    udp_port_list.append(port)
                    break
