import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 50.271055
MY_LONG = -341.176611
from_google_pass = "apje xplv jdhg urkv"
my_email = "arturtrela.automation@gmail.com"
address_email = "trela.art@gmail.com"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
sunset = 0
sunrise = 0
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
time_now = datetime.now()
act_hour = time_now.hour

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def api_data():
    global sunset, sunrise
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


api_data()

while True:
    def notification_send():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=from_google_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=address_email,
                msg=" ISS NOTIFICATON \n\n Hey! Look Up ! International Space Station Overhead "
                    "\n This mail will be send automatically from Python code "

            )


    if abs(iss_latitude - MY_LAT) < 5:
        if abs(iss_longitude - MY_LONG) < 5:
            if sunset > act_hour < sunrise:
                notification_send()
                print("Mail was send")
            else:
                print(sunset , act_hour ,sunrise)
        else:
            print("Longitude is overrange ...")
    else:
        print("To far to see ISS...")

    time.sleep(30)
    api_data()
    print(f'Latitude: {iss_latitude} / Longitude: {iss_longitude}')
