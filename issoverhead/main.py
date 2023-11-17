from dotenv import load_dotenv
import os
import smtplib
import requests
from datetime import datetime

load_dotenv()

MY_LAT = 38.722252 # Your latitude
MY_LONG = -9.139337 # Your longitude
MY_EMAIL = "test@gmail.com"
MY_PASS = os.getenv("EMAIL_PASS")

def valid_position():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  #Your position is within +5 or -5 degrees of the ISS position.

  if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude < MY_LONG + 5:
    return True

def is_dark():
  parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  time_now = datetime.now().hour
  print(time_now)
  
  if sunset <= time_now or time_now <= sunrise:
    return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if valid_position() and is_dark():
  with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(MY_EMAIL, MY_PASS)
      connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="joao_fernandess17@hotmail.com",
        msg="Subject: ISS is visible\n\nIf you look at the sky you can see the ISS"
      )

