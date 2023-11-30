import requests
from twilio.rest import Client
hours_qty = 4
auth = "25eb0ee9901d63377b251f298e0acd86"
"""Rainy localization """
localization_parameters = {
    "lat": 40.203316,
    "lon": -8.410257,
    "appid": auth,
    "units": "metric",
    "cnt": hours_qty,
}
"""My localization"""
# localization_parameters = {
#     "lat": 50.285690,
#     "lon": 18.875231,
#     "appid": auth,
#     "units": "metric",
#     "cnt": hours_qty,
# }
API_URL = f"https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(API_URL, params=localization_parameters)
response.raise_for_status()
to_show = response.json()
print(to_show)

weather_code_list=[]
for pointer in range(0, hours_qty):
    weather_code = (to_show["list"][pointer]["weather"][0]["id"])
    if weather_code < 700:
        weather_code_list.append(weather_code)
if len(weather_code_list)>0:
    print("in next 4 hours rain is possible - Take an umbrella")

account_sid = "ACe35debc71d618db5205a60f98130c727"
auth_token = "897ceea7e411db18dbd7e555e3e4c79b"
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+19562699689',
  body='W najbli¿szych godzinach przewidziany jest deszcz - Zabierz parasolkê ',
  to='+48519193352'
)

print(message.sid)
print(message.status)