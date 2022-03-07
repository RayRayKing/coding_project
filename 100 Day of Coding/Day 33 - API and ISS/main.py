import requests
import datetime as dt

# url = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url)
# response.raise_for_status()
#
# data = response.json()
# print(data["iss_position"])

url = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": 52.215933,
    "lng": 21.0067249,
    "formatted": 0
}

response = requests.get(url,params=parameters)
response.raise_for_status()


data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


now = dt.datetime.now().hour

print(sunset, sunrise, now)