from turtle import Turtle

class CreateState(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.pu()
    self.number_of_states = 0
    
  
  def state_found(self, state, x, y):
    self.goto(x, y)
    self.write(f"{state}", align = "center", font = ("courier", 15))
    self.count_states()
    
  def count_states(self):
    self.number_of_states +=1
    
  def finish(self):
    self.goto(-320, 0)
    self.write("Congrats, you found all states", font = ("courier", 25))
    