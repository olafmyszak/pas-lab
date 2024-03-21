import socket

server_address = ('localhost', 2904)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(server_address)
    while True:
        data, address = s.recvfrom(4096)
        print('Połączenie nawiązane z', address)
        data = data.decode().split()
        num1 = int(data[0])
        operator = data[1]
        num2 = int(data[2])
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            result = "Nieznany operator"

        s.sendto(str(result).encode(), address)
