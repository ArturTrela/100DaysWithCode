import requests
import datetime
API_KEY = "DoF_upgTb1msmIo7PxLjoMmdTef5GWjI"
API_ID = ""
API_SEARCH_END = "https://api.tequila.kiwi.com/v2/search"
API_LOCATION_END = "https://api.tequila.kiwi.com/locations/id"
today = datetime.datetime.today()
today = today.strftime("%d/%m/%Y")
print(today)
header = {
    'apikey':API_KEY,
}
params = {
    "id" : "KTW",
    "active_only": "true",
    "limit": 20,

}
search_params = {
    "fly_from" : "KTW",
    "date_from" : today,
    "date_to" :"07/12/2023"
}
# response = requests.get(url=API_LOCATION_END, params=params, headers=header)
# response.raise_for_status()
# resp = response.json()
# print(resp)

search_response = requests.get(url=API_SEARCH_END, params=search_params ,headers=header)
search_response.raise_for_status()
search_data = search_response.json()
cityCode_to = search_data['data'][0]['cityCodeTo']
cityName_to = search_data['data'][0]['cityTo']
flight_price = search_data['data'][0]['price']

print(cityName_to , cityCode_to , flight_price)

class FlightSearch:
    pass