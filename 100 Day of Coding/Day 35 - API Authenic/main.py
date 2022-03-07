import requests
import os
from twilio.rest import Client

API_KEY = "260dd82542030b49b38d18fcc264d876"
URL = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
    "lat": 50.064651,
    "lon": 19.944981,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# account_sid = 'AC7f74e0bd88bd9f015c4e1b099793084b'
auth_token = '81a164a2f5c1c4f19c2dfb4575ad5b63'
account_sid = os.environ.get("account_sid")
print(account_sid)




response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()

data = response.json()

# TRaverse strucutre  dic -> hourly(increment) -> weather -> firstposition ID -> id
# data["hourly"][x]["weather"][0]["id"]
will_rain = False

hourly_id = []
for x in range(0, 13):
    id_code = data["hourly"][x]["weather"][0]["id"]
    hourly_id.append(id_code)
    if id_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember in bring an umbrellaa",
        from_='+17372019105',
        to='+15103260730'
    )
    print(message.status, message.sid)

