import socket

# Definiujemy adres i port serwera
host = 'httpbin.org'
port = 80
path = '/html'

# Tworzymy gniazdo (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Łączymy się z serwerem
s.connect((host, port))

# Przygotowujemy żądanie HTTP
request = f"GET {path} HTTP/1.1\r\n" \
          f"Host: {host}\r\n" \
          f"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n" \
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

# Zapisujemy treść strony HTML do pliku
with open("page.html", "wb") as f:
    f.write(body)
