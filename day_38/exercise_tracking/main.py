import requests
from datetime import datetime
APP_ID = "7243a9be"
API_KEY = "6774f87bb86acd9990011b48e575bcbd"

NUTRIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/1f5d6c349b86c0951545c5242f55b446/myWorkouts/workouts"
query = input()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params_nutrix = {
    'query': query,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 180.64,
    "age": 20
}

response = requests.post(
    url=NUTRIX_ENDPOINT, json=params_nutrix, headers=headers)
r = response.json()

for exercise in r["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)
print(sheet_response.text)
