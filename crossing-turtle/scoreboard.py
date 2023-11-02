from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.pu()
    self.hideturtle()
    self.goto(-220, 260)
    self.level = 1
    self.update_level()
    
  def update_level(self):
    self.write(f"Level: {self.level}", align = "center", font = ("courier", 20))
  
  def calculate_level(self):
    self.level += 1
    self.clear()
    self.update_level()
    
  def game_over(self):
    self.goto(0, 0)
    self.write(f"GAME OVER", align="center", font=("courier", 20))