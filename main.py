import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "abcd.com"
MY_PASS = "abcd()"

MY_LAT = 30.969349
MY_LONG = 70.942795
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response)
    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print(iss_position)
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()
    data = sunset_response.json()
    # print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    print(time_now.hour)
    if time_now >= sunset or time_now <= sunrise:
        return True 

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\n The ISS above you in the sky"


wjkkdkgmfcfkld
kdlfkeotuibudiy
        )
        

