from turtle import Turtle

class Frog(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("white")
    self.pu()
    self.frog_reset()
    self.setheading(90)
    
  def move_up(self):
    self.setheading(90)
    self.fd(20)
    
  def move_down(self):
    self.setheading(270)
    self.fd(20)
    
  def frog_reset(self):
    self.goto(0, -260)