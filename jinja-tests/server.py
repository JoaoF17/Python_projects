from flask import Flask, render_template
from datetime import date
import requests

name = "João Fernandes"
year = str(date.today()).split("-")[0]

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html", name=name, year=year)

@app.route("/<name_input>")
def names_route(name_input):
  age_response = requests.get(f"https://api.agify.io/?name={name_input}")
  age = age_response.json()['age']
  gender_response = requests.get(f"https://api.genderize.io?name={name_input}")
  gender = gender_response.json()['gender']
  return render_template("name.html", name=name, year=year, name_fetch=name_input, gender=gender, age=age)

if __name__ == "__main__":
  app.run(debug=True)