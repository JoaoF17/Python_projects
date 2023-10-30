from turtle import Turtle
from random import randrange

class Food(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
    self.color("red")
    self.speed("fastest")
    self.refresh()
    
  def refresh(self):
    x_coordinate = randrange(-280, 280, 20)
    y_coordinate = randrange(-280, 280, 20)
    self.goto(x_coordinate, y_coordinate)