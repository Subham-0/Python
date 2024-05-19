
from time import time
import requests
from datetime import datetime

import smtplib

MY_EMAIL= "testsmtpcode11@gmail.com"
MY_PASSWORD = "engo deew tjid zqeh"


MY_LAT = 20.296059
MY_LNG = 85.824539

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status() 

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude =float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
def is_night():      
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG, 
        "formatted" : 0 ,
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)  
    if iss_overhead() and is_night():
        connection  =  smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs="dashsubham2002@gmail.com",msg="Subject:Look up👆🏽\n\nThe ISS is above you in the sky")