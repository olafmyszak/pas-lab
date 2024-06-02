import requests


def get_user_input():
    # Pobieranie danych od użytkownika
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    message = input("Enter your message: ")
    return {"name": name, "email": email, "message": message}


def send_post_request(data):
    # Definiujemy adres URL
    url = "http://httpbin.org/post"

    # Przygotowujemy nagłówki
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Wysyłamy żądanie POST
    response = requests.post(url, headers=headers, data=data)

    # Zwracamy odpowiedź z serwera
    return response



user_data = get_user_input()

# Wysyłamy żądanie POST
response = send_post_request(user_data)

# Wyświetlamy odpowiedź z serwera
print("Status Code:", response.status_code)
print("Response Body:", response.text)
