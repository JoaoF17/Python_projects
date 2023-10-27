from turtle import Turtle, Screen

tim =  Turtle()
screen = Screen()

def move_forward():
  tim.fd(50)

def move_up():
  tim.setheading(90)
  tim.fd(50)
  
def move_down():
  tim.setheading(270)
  tim.fd(50)
  
def move_right():
  tim.setheading(0)
  tim.fd(50)
  
def move_left():
  tim.setheading(180)
  tim.fd(50)
  
def reset():
  screen.resetscreen()


screen.listen()
screen.onkey(fun = move_forward, key = "space")
screen.onkey(fun = move_up, key = "w")
screen.onkey(fun = move_down, key = "s")
screen.onkey(fun = move_right, key = "d")
screen.onkey(fun = move_left, key = "a")
screen.onkey(fun = reset, key = "r")
screen.exitonclick()