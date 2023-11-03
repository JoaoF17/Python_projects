from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.total_score = 0
    with open("data.txt") as data:
      self.high_score = int(data.read())
    self.color("white")
    self.penup()
    self.goto(0, 250)
    self.hideturtle()
    self.update_score()
    
  def update_score(self):
    self.clear()
    self.write(f"Score:{self.total_score} || Highscore:{self.high_score}", align = "center", font = ("courier", 25))
    
  def calculate_score(self):
    self.total_score += 1
    self.update_score()
    
  def game_over(self):
    self.goto(0, 0)
    self.write(f"Game Over", align = "center", font = ("courier", 25))
    
  def reset(self):
    if self.total_score > self.high_score:
      self.high_score = self.total_score
      with open("data.txt", mode="w") as data:
        data.write(f"{self.total_score}")
    self.total_score = 0
    self.update_score()