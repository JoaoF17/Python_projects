import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

ID = os.getenv("NUTRI_ID")
KEY = os.getenv("NUTRI_KEY")

SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEETY_PASS = os.getenv("SHEETY_PASS")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
  "x-app-id": ID,
  "x-app-key": KEY,
  "Content-Type": "application/json"
}

user_input = input("Tell me which exercise you did: ")

post_body = {
  "query":user_input,
  "gender":"female",
  "weight_kg":72.5,
  "height_cm":167.64,
  "age":30
}

response = requests.post(url=nutri_endpoint, json=post_body, headers=headers)
data =response.json()
print(response.text)
print(data)

#sheety API
username = "joaof17"
project_name = "My Workouts"
sheet_name = "My Workouts"

day = datetime.now()
today_date = day.strftime("%Y/%m/%d")
today_time = day.strftime("%H:%M:%S")

exercise =  data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

sheety_headers = {
  "Authorization": SHEETY_AUTH
}

sheety_params = {
  "workout":{
    "date": today_date,
    "time": today_time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
  }
}

sheety_endpoint = "https://api.sheety.co/b65805a12938a6c063ec5c9ed24e8287/myWorkouts/workouts"

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
data = response.json()
print(response.text)