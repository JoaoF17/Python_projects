import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = "joaof17"
TOKEN = os.getenv("PIXELO_TOKEN")
GRAPH_ID = "graph1"

#reusable vars
pixela_endpoint = "https://pixe.la/v1/users"

headers ={
  "X-USER-TOKEN": TOKEN
}

day = datetime(year=2023, month=11, day=21)
date = day.strftime("%Y%m%d")

#------Creating user------#
user_parameters = {
  "token": "",
  "username": "joaof17",
  "agreeTermsOfService":  "yes",
  "notMinor": "yes"
}

# post_response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(post_response.status_code)

#------create graph------#
graph_parameters = {
  "id": "graph1",
  "name": "Running Graph",
  "unit": "Km",
  "type": "float",
  "color": "shibafu" 
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_reponse = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_reponse.status_code)


#------post a pixel in the graph------#
pixel_params = {
  "date": date, #convert the time to required time format
  "quantity": "3.43"
}

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(pixel_response.text)

#------update a pixel (put)------#
update_pixel_params = {
  "quantity" : "1.2"
}

put_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# put_response = requests.put(url=put_delete_endpoint, json=update_pixel_params, headers=headers)
# print(put_response.text)

#------delete a pixel (delete)------#
# delete_reponse = requests.delete(url=put_delete_endpoint, headers=headers)
# print(delete_reponse.text)