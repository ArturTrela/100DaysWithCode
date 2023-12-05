# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

CITIES = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
CODES =[]
flightSearch = FlightSearch()
# founded_flight = flight_search.flightCheck()
# print(founded_flight)

# _________________ TAKE DATA FROM GOOGLE SHEETS_____________
sheetData = DataManager()
datasheet = sheetData.take_data_from_sheet()
cities_name =[]
for city in datasheet:
    city_name = city['city']
    ident = city['id']
    miasta ={
        city_name : ident
    }
    cities_name.append(miasta)

# ____________UPDATE AIRPORT'S CODES IN FILE _____________
is_required_update_codes = False
if is_required_update_codes:
    ident = 2
    for name in CITIES:
        code = flightSearch.takeName(name)
        CODES.append(code)
        sheetData.codeFilling( code, name, ident)
        ident +=1
else:
    print(F'File is actual ')