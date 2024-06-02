import socket
import os


def handle_request(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    headers = request.split('\r\n')
    request_line = headers[0].split(' ')
    method = request_line[0]
    path = request_line[1]

    if method == 'GET':
        if path == '/':
            response = serve_file('index.html', '200 OK')
        else:
            file_path = path.lstrip('/')
            if os.path.exists(file_path):
                response = serve_file(file_path, '200 OK')
            else:
                response = serve_file('404.html', '404 Not Found')
    else:
        response = serve_file('405.html', '405 Method Not Allowed')

    client_socket.sendall(response)
    client_socket.close()


def serve_file(file_path, status_code):
    try:
        with open(file_path, 'rb') as f:
            body = f.read()
    except IOError:
        body = b"Error reading file"

    headers = [
        f'HTTP/1.1 {status_code}',
        'Content-Type: text/html; charset=utf-8',
        f'Content-Length: {len(body)}',
        'Connection: close',
        '\r\n'
    ]

    response = '\r\n'.join(headers).encode('utf-8') + body
    return response


def run_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_request(client_socket)


run_server()
