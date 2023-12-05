import requests
import datetime

API_KEY = "DoF_upgTb1msmIo7PxLjoMmdTef5GWjI"
API_ID = ""
API_SEARCH_END = "https://api.tequila.kiwi.com/v2/search"
API_LOCATION_END = "https://api.tequila.kiwi.com/locations/query"
today = datetime.datetime.today()
today = today.strftime("%d/%m/%Y")


class FlightSearch:

    def __init__(self):
        self.header = {
            "apikey": API_KEY,
        }
        self.flight_values =[]

    def flightCheck(self):
        search_params = {
            "fly_from": "KTW",
            "date_from": today,
            "date_to": "07/12/2023",
            # "curr" : tutaj wpisac f-string z kodami IATA z googla,
            "limit": "10",
        }
        search_response = requests.get(url=API_SEARCH_END, params=search_params, headers=self.header)
        search_response.raise_for_status()
        search_data = search_response.json()

        #### Concept of grab value ####
        for data in search_data['data']:
            cityCode_to = data['cityCodeTo']
            cityName_to = data['cityTo']
            flight_price = data['price']
            flight_price_currency = data['conversion']
            flight_params = {
                "city": cityName_to,
                "cityCode": cityCode_to,
                "price": flight_price,
                "currency": flight_price_currency,
            }
            self.flight_values.append(flight_params)

        return self.flight_values

    def takeName(self,name):
        name_params ={
            "term" : name
        }

        response_iata= requests.get(url=API_LOCATION_END, params=name_params, headers=self.header)
        response_iata.raise_for_status()
        result = response_iata.json()
        city_code = result['locations'][0]['code']

        return city_code
