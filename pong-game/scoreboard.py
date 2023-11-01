from turtle import Turtle

class Scoreboard(Turtle):
  
  def __init__(self, player):
    super().__init__()
    self.color("white")
    self.pu()
    self.hideturtle()
    if player == 1:
      self.goto(-50, 260)
    elif player == 2:
      self.goto(50, 260)
    self.total_score = 0
    self.update_score()
    
  def update_score(self):
    self.write(f"{self.total_score}", align = "center", font = ("courier", 25))
  
  def calculate_score(self):
    self.total_score += 1
    self.clear()
    self.update_score()
    