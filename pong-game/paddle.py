from turtle import Turtle

WIDTH = 5
HEIGHT = 1
STARTING_POSITION_P1 = (-360, 0)
STARTING_POSITION_P2 = (360, 0)

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.pu()
    self.setheading(90)
    self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
    if position == "left":
      self.goto(x=STARTING_POSITION_P1[0], y=STARTING_POSITION_P1[1])
    elif position == "right":
      self.goto(x=STARTING_POSITION_P2[0], y=STARTING_POSITION_P2[1])
    
  def up(self):
    if self.ycor() < 260: 
      self.setheading(90)
      self.fd(20)
  
  def down(self):
    if self.ycor() > -260:
      self.setheading(270)
      self.fd(20)
