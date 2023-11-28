import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SHEETY_AUTH = os.getenv("SHEETY_AUTH_FLIGHTS")
SHEETY_PASS = os.getenv("SHEETY_PASS_FLIGHTS")
SHEETY_ENDPOINT = "https://api.sheety.co/b65805a12938a6c063ec5c9ed24e8287/flightDeals/prices"

headers = {
      "Authorization": SHEETY_AUTH
    }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
      self.destination_data = {}

    def get_destination_data(self):
      response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
      data = response.json()
      self.destination_data = data["prices"]
      return self.destination_data
    
    def update_destination_codes(self):
      for city in self.destination_data:
        new_data = {
          "price": {
            "iataCode": city["iataCode"]
          }
        }
        response = requests.put(
          url=f"{SHEETY_ENDPOINT}/{city['id']}",
          json=new_data,
          headers=headers
        )
        print(response.text)