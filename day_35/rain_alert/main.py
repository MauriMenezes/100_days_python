import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "36dfdb1140c9699f97a449028f3fbb8b"

account_sid = "AC6c6af9a61865119b43ee5fe16b08d40f"
auth_token = "edaaae955d10c5b9ffc64b7adc393b6f"


params = {
    'lat': -12.918831,
    'lon': -38.631188,
    "appid": api_key,
    'exclude': "current,minutely,daily"
}

response = requests.get(
    ENDPOINT, params=params)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:20]

rain = False
for i in weather_slice:
    condition_code = i['weather'][0]['id']
    # print(condition_code)
    if condition_code <= 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='vai chover',
        to='whatsapp:+557186754350'
    )

    print(message.sid)
