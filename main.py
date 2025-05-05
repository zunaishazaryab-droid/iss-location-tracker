import requests

response = requests.get(url="http://api.open-notify.org/iss-nows.json")
print(response)
if response.status_code == 404:
    raise Exception("The thing you are looking for not exists")
else:
    print("Here you Go")

