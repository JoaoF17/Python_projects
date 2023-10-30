from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.total_score = 0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.update_score()
    
  def update_score(self):
    self.goto(0, 250)
    self.write(f"Score: {self.total_score}", align = "center", font = ("courier", 25))
    
  def calculate_score(self):
    self.total_score += 1
    self.clear()
    self.update_score()
    
  def game_over(self):
    self.goto(0, 0)
    self.write(f"Game Over", align = "center", font = ("courier", 25))