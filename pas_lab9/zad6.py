import os
import socket
from datetime import datetime

# Definiujemy adres i port serwera
host = '212.182.24.27'
port = 8080
path = '/image.jpg'
image_path = "image.jpg"
last_modified_time = None

# Sprawdzenie, czy istnieje plik z zapisaną datą ostatniej modyfikacji
if os.path.exists(image_path):
    last_modified_time = os.path.getmtime(image_path)
    last_modified_time = datetime.utcfromtimestamp(last_modified_time).strftime('%a, %d %b %Y %H:%M:%S GMT')

# Tworzymy gniazdo (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Łączymy się z serwerem
s.connect((host, port))

# Przygotowujemy żądanie HTTP
request = f"GET {path} HTTP/1.1\r\n" \
          f"Host: {host}\r\n" \
          f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"

if last_modified_time:
    request += f"If-Modified-Since: {last_modified_time}\r\n"

request += "Connection: close\r\n\r\n"

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

# Przetwarzamy nagłówki
headers = headers.decode().split("\r\n")
status_line = headers[0]
status_code = int(status_line.split()[1])

if status_code == 200:
    # Zapisujemy obrazek do pliku
    with open(image_path, "wb") as f:
        f.write(body)

    # Aktualizujemy czas modyfikacji pliku
    for header in headers:
        if header.startswith("Last-Modified"):
            last_modified = header.split(": ", 1)[1]
            last_modified_time = datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S GMT')
            os.utime(image_path, (last_modified_time.timestamp(), last_modified_time.timestamp()))

    print("Image downloaded and saved.")
elif status_code == 304:
    print("Image has not been modified since the last download.")
else:
    print(f"Failed to fetch image. HTTP Status Code: {status_code}")
