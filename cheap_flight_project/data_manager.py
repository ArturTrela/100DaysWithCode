import requests


class DataManager:
    def __init__(self):
        self.BEARER = "Bearer @Automation@Automatyk2023"
        self.API_GET_END = "https://api.sheety.co/4e668c043186844af25349f9dcd69fdc/flightDeals/prices"
        self.sheet_headers = {
            "Authorization": self.BEARER,
        }

    def take_data_from_sheet(self):
        response = requests.get(url=self.API_GET_END, headers=self.sheet_headers)
        response.raise_for_status()
        data_from_sheets = response.json()

        return data_from_sheets
