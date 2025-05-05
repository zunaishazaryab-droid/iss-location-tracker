import requests
from datetime import datetime

MY_LAT = 30.969349
MY_LONG = 70.942795

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
parameters = {
    "lat":MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sunset_response.raise_for_status()
data = sunset_response.json()
# print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

date_now = datetime.now()
print(date_now.hour)

