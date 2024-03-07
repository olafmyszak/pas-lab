import socket

server_address = ('localhost', 2902)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(server_address)
    print('Server started...')
    while True:
        data, address = s.recvfrom(4096)
        print(f'Received {data} from {address}')
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
            result = 'Invalid operator'

        s.sendto(str(result).encode(), address)
