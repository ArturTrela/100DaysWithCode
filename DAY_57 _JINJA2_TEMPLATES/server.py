from flask import Flask , render_template
import random
import datetime as dt
import requests
app = Flask(__name__)

@app.route('/')
def index():
    random_numer = random.randint(1,10)
    year= dt.datetime.now().year
    return render_template('index.html', numer=random_numer, rok =year)


@app.route('/guess/<name>')
def check_name_age(name):
    imie = str(name).capitalize()
    search_response = requests.get(url=f"https://api.agify.io?name={imie}" )
    search_response.raise_for_status()
    search_data = search_response.json()
    wiek = search_data['age']

    search_response2 = requests.get(url=f"https://api.genderize.io?name={imie}")
    search_response2.raise_for_status()
    search_data2 = search_response2.json()
    plec = search_data2['gender']
    if plec == 'male':
        plec = 'mężczyzna'
    else:
        plec = 'kobieta'
    return render_template('guess.html', imie= imie, wiek=wiek, plec=plec)


if __name__ == '__main__':
    app.run(debug = True)