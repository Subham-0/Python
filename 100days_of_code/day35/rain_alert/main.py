import geocoder
import requests
from twilio.rest import Client

api_key = "6fb3e2180e4d00f9e41c8beedf5a7ab6"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "REPLACE_WITH_ACTUAL_SID"
auth_token ="REPLACE_WITH_ACTUAL_TOKEN"

myloc = geocoder.ip('me')
my_loc_list = myloc.latlng
my_lat = my_loc_list[0]
my_lng = my_loc_list[1]

wheather_params ={
    "lat":my_lat,
    "lon":my_lng,
    "appid":api_key,
    "cnt":4, 
}

response = requests.get(url=OWM_Endpoint,params=wheather_params)

response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☔",
                        from_='+12183072150',
                        to='+919348815542,'
                    )
    print(message.status)



