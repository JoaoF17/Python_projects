from twilio.rest import Client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API")

account_sid = os.getenv("WA_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
  "lat": 13.756331,
  "lon": 100.501762,
  "exclude": "current,minutely,daily,alerts",
  "appid": API_KEY
}

response = requests.get(url= "https://api.openweathermap.org/data/2.8/onecall", params=parameters)
data= response.json()
# print(data1["hourly"][0]["weather"][0]["id"])

hours = data["hourly"]

bad_weather = False
for hour in hours[:7]:
  print(hour["weather"])
  if hour["weather"][0]["id"] < 700:
    bad_weather = True

message = client.messages.create(
  from_= os.getenv("FROM_NUMBER"),
  body='Bring an Umbrella.',
  to=os.getenv("TO_NUMBER")
)

if bad_weather:
  print(message.sid)

