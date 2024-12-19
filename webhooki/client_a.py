import requests
import json

def send_data(data):
    url = 'http://localhost:5000/webhook'  # Adres URL klienta B
    response = requests.post(url, json=data)
    print(f"Odpowiedz od klienta B: {response.json()}")

if __name__ == '__main__':
    data_to_send = {
        "name": "Jan Kowalski",
        "email": "jan.kowalski@example.com",
        "message": "To jest testowy komunikat."
    }
    send_data(data_to_send)