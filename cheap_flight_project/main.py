# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
flight_search = FlightSearch()
founded_flight = flight_search.flightCheck()
print(founded_flight)

sheet_data = DataManager()
datasheet = sheet_data.take_data_from_sheet()
print(datasheet)