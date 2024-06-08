import socket
import ssl


def fetch_html():
    request = "GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Safari/7.0.3\r\n\r\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        ssl_client_socket = ssl.wrap_socket(client_socket)

        ssl_client_socket.connect(('httpbin.org', 443))

        ssl_client_socket.sendall(request.encode())

        response = ssl_client_socket.recv(4096)

    html_content = response.split(b'\r\n\r\n')[1]
    print(html_content.decode())


fetch_html()
