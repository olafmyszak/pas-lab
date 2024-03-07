import socket

server_address = ('localhost', 2902)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    client.connect(server_address)

except socket.error as e:
    print(e)

else:
    num1 = input('Enter first number: ')
    operator = input('Enter operator: ')
    num2 = input('Enter second number: ')
    client.sendto(f'{num1} {operator} {num2}'.encode(), server_address)
    result, address = client.recvfrom(4096)
    print(f'Result: {result.decode()}')

client.close()
