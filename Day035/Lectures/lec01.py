import requests
from sys import argv

LATITUDE = -22.338930
LONGITUDE = -49.055190

api_key = argv[1]
api_url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key
}

response = requests.get(api_url, params=params)

data = response.json()
print(data)
