import requests
#
APP_ID = "2abc9635"
API_KEY = "36c3ef0d5700ad87439dfbc0d140e0d7"
API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_end = "https://api.sheety.co/4e668c043186844af25349f9dcd69fdc/myWorkouts/workouts"

headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}
# # query = input("Tell me exercise and time")
test_query = "Swam for 1 hour"
body = {
    "query": test_query,
    "age": "30",
    "gender": "male",
    "weight_kg": "84",
    "height_cm": "185",
}

response = requests.post(url=API_URL, json=body, headers=headers)
response.raise_for_status()
result = response.json()
print(result["exercises"])


