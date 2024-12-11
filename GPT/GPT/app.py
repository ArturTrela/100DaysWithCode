from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime
from matplotlib.dates import DateFormatter


app = Flask(__name__)

API_KEY = "f3b335241a8588b71fd0abf09f3fa7a2"  # Podstaw swój klucz API
BASE_URL = "http://data.fixer.io/api/"
currencies = ["USD", "EUR", "GBP", "CHF", "CAD", "AUD"]


# Funkcja do pobierania kursów walut z ostatnich 24 godzin
def get_exchange_rates_24h(currency):
    url = f"{BASE_URL}timeseries?access_key={API_KEY}&start_date={datetime.now().strftime('%Y-%m-%d')}&end_date={datetime.now().strftime('%Y-%m-%d')}&symbols={currency}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Błąd ładowania danych dla {currency}. Status kod: {response.status_code}")
        return [], []

    data = response.json()

    # Wydobywanie danych
    dates = list(data['rates'].keys())
    values = [data['rates'][date][currency] for date in dates]

    return dates, values


# Funkcja do generowania wykresu dla kursu
def generate_chart(currency):
    dates, values = get_exchange_rates_24h(currency)

    if not dates or not values:
        return None

    fig, ax = plt.subplots(figsize=(6, 3))

    # Rysowanie wykresu
    ax.plot(dates, values, marker='o', color='tab:blue')
    ax.set_title(f'Kurs {currency} z ostatnich 24h')
    ax.set_xlabel('Data')
    ax.set_ylabel('Kurs')

    # Formatowanie dat
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

    # Zapisz wykres do bufora w formacie PNG
    img_buf = io.BytesIO()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Przekształć wykres na kod base64, aby można było go wyświetlić w HTML
    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    plt.close(fig)

    return img_base64


@app.route('/')
def index():
    return render_template('index.html', currencies=currencies)


@app.route('/waluty')
def waluty():
    charts = {}
    for currency in currencies:
        img_base64 = generate_chart(currency)
        charts[currency] = img_base64
    return render_template('waluty.html', charts=charts, currencies=currencies,
                           current_date=datetime.now().strftime("%Y-%m-%d"))


if __name__ == '__main__':
    app.run(debug=True)
