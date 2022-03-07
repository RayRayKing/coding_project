import requests
from datetime import datetime
USERNAME = "rayray"
TOKEN = "efawefaefafllwe23124sd"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "efawefaefafllwe23124sd",
    "username": "rayray",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
# #create account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Push-up Graph",
    "unit": "Count",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# #create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

data_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"
#date format:yyyyMMdd

today = datetime.now()

data_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many push-ups did you do in total!?!"),
}
# create a data
response = requests.post(url=data_endpoint,json=data_config,headers=headers)
(print(response.text))

# update a data

# put_data_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
# data_update = {
#     "quantity": "12"
# }

# delete_data_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}/{'20211124'}"
# response = requests.delete(url=delete_data_endpoint, headers=headers)
# print(response.text)
#
