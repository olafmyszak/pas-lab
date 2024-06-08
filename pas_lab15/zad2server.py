import socket

import requests


def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Lublin",
        "appid": "d4af3e33095b8c43f1a6815954face64"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        return f"Current weather in Lublin: {weather}, temperature: {temperature:.2f}°C"
    else:
        return "Failed to retrieve weather information"


server_host = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_host, server_port))

server_socket.listen(5)

print(f"Server listening on {server_host}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    weather_info = get_weather()
    client_socket.sendall(weather_info.encode())

    client_socket.close()
