import socket


def fetch_image_partially(host, port, path, start, end):
    # Tworzymy gniazdo (socket)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Łączymy się z serwerem
    s.connect((host, port))

    # Przygotowujemy żądanie HTTP z nagłówkiem Range
    request = f"GET {path} HTTP/1.1\r\n" \
              f"Host: {host}\r\n" \
              f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n" \
              f"Range: bytes={start}-{end}\r\n" \
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

    return body


def fetch_image():
    # Definiujemy adres i port serwera
    host = '212.182.24.27'
    port = 8080
    path = '/image.jpg'

    # Definiujemy zakresy bajtów do pobrania
    part1 = fetch_image_partially(host, port, path, 0, 99999)
    part2 = fetch_image_partially(host, port, path, 100000, 199999)
    part3 = fetch_image_partially(host, port, path, 200000, 299999)

    # Łączymy części w całość
    image_data = part1 + part2 + part3

    # Zapisujemy obrazek do pliku
    with open("image.jpg", "wb") as f:
        f.write(image_data)


# Wywołujemy funkcję pobierającą i zapisującą obrazek
fetch_image()
