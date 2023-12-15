from flask import Flask
from random import randint

app = Flask(__name__)

def random_number():
  num = randint(0,9)
  print(num) 
  return num

@app.route("/")
def home():
  return "<h1>Guess a number between 0 and 9.</h1><img src='https://media.giphy.com/media/W6bZ7NNFlS8PGx2fPo/giphy.gif'>"

@app.route("/<int:number>")
def chosen_number(number):
  correct_number = random_number()
  if correct_number < number:
    return f"<h2 style='color:blue;'>{number} is too high, try again!</h2>"
  elif correct_number > number:
    return f"<h2 style='color:red;'>{number} is too low, try again!</h2>"
  else:
    return f"<h2 style='color:green;'>Well done! {number} is the right number!</h2>"

if __name__ == "__main__":
  app.run(debug=True)