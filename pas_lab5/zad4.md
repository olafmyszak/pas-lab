# Serwer TCP

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

client_socket, address = server_socket.accept()

data = client_socket.recv(1024)
client_socket.sendall(data)

client_socket.close()
server_socket.close()
```

# Klient TCP

```python
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

start_time = time.time()
client_socket.sendall(b'Hello, TCP server!')
data = client_socket.recv(1024)
end_time = time.time()

print("Odebrano:", data.decode())
print("Czas przesyłu:", end_time - start_time, "sekund")

client_socket.close()
```

# Serwer UDP

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

data, address = server_socket.recvfrom(1024)
server_socket.sendto(data, address)

server_socket.close()
```

# Klient UDP

```python
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start_time = time.time()
client_socket.sendto(b'Hello, UDP server!', ('localhost', 12345))
data, _ = client_socket.recvfrom(1024)
end_time = time.time()

print("Odebrano:", data.decode())
print("Czas przesyłu:", end_time - start_time, "sekund")

client_socket.close()
```

# Dla którego z gniazd czas jest krótszy?

Czas przesyłu może być krótszy dla gniazda UDP.

# Z czego wynika krótszy czas?

Krótszy czas przesyłu danych za pomocą gniazda UDP może wynikać z braku procesu nawiązywania połączenia i kontroli
przepływu, które są obecne w gnieździe TCP.

# Jakie są zalety / wady obu rozwiązań?

|                     	                     |  TCP  	  |  UDP   	   |
|:-----------------------------------------:|:--------:|:----------:|
|      szybkość przesyłu            	       | niska 	  | wysoka  	  |
|        niezawodność              	        | wysoka 	 |  niska  	  |
|   wykrywanie i korygowanie błędów     	   |  tak  	  |  nie   	   |
|    potwierdzenie odbioru danych      	    | zawsze 	 | checksum 	 |
| kontrola powstawania zatorów w przesyle 	 | zawsze 	 |  nie   	   |
