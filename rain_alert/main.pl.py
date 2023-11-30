import requests
hours_qty = 4
"""Rainy localization """
localization_parameters = {
    "lat": 40.203316,
    "lon": -8.410257,
    "appid": "25eb0ee9901d63377b251f298e0acd86",
    "units": "metric",
    "cnt": hours_qty,
}
"""My localization"""
# localization_parameters = {
#     "lat": 50.285690,
#     "lon": 18.875231,
#     "appid": "25eb0ee9901d63377b251f298e0acd86",
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
