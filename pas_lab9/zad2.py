import socket

# Definiujemy adres i port serwera
host = 'httpbin.org'
port = 80
path = '/image/png'

# Tworzymy gniazdo (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Łączymy się z serwerem
s.connect((host, port))

# Przygotowujemy żądanie HTTP
request = f"GET {path} HTTP/1.1\r\n" \
          f"Host: {host}\r\n" \
          f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n" \
          f"Connection: close\r\n\r\n"

# Wysyłamy żądanie do serwera
s.sendall(request.encode())

# Odbieramy odpowiedź z serwera
response = b""
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    response += chunk

# Zamykamy połączenie
s.close()

# Rozdzielamy nagłówki od treści
headers, body = response.split(b"\r\n\r\n", 1)

# Zapisujemy obrazek do pliku
with open("image.png", "wb") as f:
    f.write(body)
