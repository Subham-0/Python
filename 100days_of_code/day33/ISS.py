import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status() 

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude =float(data["iss_position"]["latitude"])

is_position = (longitude,latitude)
print(is_position)