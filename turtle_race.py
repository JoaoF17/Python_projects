from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the reace? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x = -230, y = y_positions[turtle_index])
  all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You guessed it! The {winning_color} turtle is the winner.")
      else:
        print(f"You picked the wrong turtle. The {winning_color} turtle is the winner.")
      is_race_on = False
    
    random_distance = randint(0, 10)
    turtle.fd(random_distance)

screen.exitonclick()