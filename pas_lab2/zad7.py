import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (sys.argv[1], int(sys.argv[2]))

try:
    sock.connect(server_address)
    print('port otwarty')

    try:
        service = socket.getservbyport(int(sys.argv[2]))
    except socket.error as e:
        print("brak usług")
    else:
        print(f'usluga: {service}')


except socket.error as e:
    print(e)
