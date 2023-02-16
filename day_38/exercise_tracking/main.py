import requests
import datetime
APP_ID = "MYAPP ID FROM NUTRITIONIX API"
API_KEY = "MYAPP API_KEY FROM NUTRITIONIX APi"

NUTRIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "MY GOOGLE SHEET_ENDPOINT"
query = input()

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

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
