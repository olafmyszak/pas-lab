import json
import socket
import ssl


def get_weather(city):
    api_key = 'd4af3e33095b8c43f1a6815954face64'
    host = 'api.openweathermap.org'
    port = 443

    with socket.create_connection((host, port)) as client_socket:
        ssl_client_socket = ssl.wrap_socket(client_socket)

        request = f"GET /data/2.5/weather?q={city}&appid={api_key}&units=metric HTTP/1.1\r\nHost: {host}\r\nUser-Agent: IRC_Bot\r\n\r\n"

        ssl_client_socket.sendall(request.encode())

        response = ssl_client_socket.recv(4096).decode()

    weather_data = json.loads(response)
    if 'main' in weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return f"The weather in {city} is {description} with a temperature of {temperature}°C."
    else:
        return "Failed to retrieve weather information."


def handle_message(message):
    city = message.split()[1]
    return get_weather(city)


server = 'chat.freenode.net'
port = 7000
nickname = 'MyBot'
channel = '#mychannel'

irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc_socket.connect((server, port))

irc_socket.sendall(f"NICK {nickname}\r\n".encode())
irc_socket.sendall(f"USER {nickname} 0 * :{nickname}\r\n".encode())

irc_socket.sendall(f"JOIN {channel}\r\n".encode())

while True:
    message = irc_socket.recv(2048).decode()

    if 'PRIVMSG' in message:
        response = handle_message(message)
        irc_socket.sendall(f"PRIVMSG {channel} :{response}\r\n".encode())
