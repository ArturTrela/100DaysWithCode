import requests
import os

BEARER = "Bearer @Automation@Automatyk2023"
API_GET_END = "https://api.sheety.co/4e668c043186844af25349f9dcd69fdc/flightDeals/prices"
sheet_headers = {
    "Authorization": BEARER,
}


class DataManager:
    def __init__(self):
        pass

    response = requests.get(url=API_GET_END, headers=sheet_headers)
    response.raise_for_status()
    data_from_sheets = response.json()
    print(data_from_sheets)
