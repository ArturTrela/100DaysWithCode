import requests
import datetime

# CONSTANTS #
APP_ID = "2abc9635"
API_KEY = "36c3ef0d5700ad87439dfbc0d140e0d7"
API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_END = "https://api.sheety.co/4e668c043186844af25349f9dcd69fdc/myWorkouts/workouts"

# Take an actual hour and day #

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
hour = today.strftime("%H:%M:%S")

# header for natural language
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

# Take a sentence from user # ( Test query / User input query )
query = input("Tell me exercise and time")
# test_query = "Swam for 1 hour"

# Body for query to natural language - for this case in HARD CODING way
body = {
    "query": query,
    "age": "30",
    "gender": "male",
    "weight_kg": "84",
    "height_cm": "185",
}

# Make a query for nutritonix
response = requests.post(url=API_URL, json=body, headers=headers)
response.raise_for_status()
result = response.json()

# Preparation data from response json nutritonix to use in sheety
workout_time = result['exercises'][0]["duration_min"]
workout_type = result['exercises'][0]["name"]
workout_calories = result['exercises'][0]["nf_calories"]

sheet_params = {
    "workout": {
            "date": date,
            "time": hour,
            "exercise": workout_type,
            "duration": workout_time,
            "calories": workout_calories,
    }
}
sheety_response = requests.post(url=SHEETY_END, json=sheet_params)
sheety_response.raise_for_status()
result_sheets = sheety_response.json()
print(result_sheets)
