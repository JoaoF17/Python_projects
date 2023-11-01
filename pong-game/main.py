from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle1 = Paddle("left")
paddle2 = Paddle("right")
score1 = Scoreboard(1)
score2 = Scoreboard(2)

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball = Ball()

game_on = True
while game_on:
  sleep(ball.move_speed)
  screen.update()
  ball.move()

  # detect bounce on upper and lower walls and when game is lost
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_walls()
  
  #detect collision with paddle
  if ball.distance(paddle2) < 50 and ball.xcor() > 330 or ball.distance(paddle1) < 50 and ball.xcor() < -330:
    ball.bounce_paddles()
  
  # paddle 2 loses
  if ball.xcor() > 400:
    # Add scoreboard notice that game i
    ball.reset()
    score1.calculate_score()
    screen.update()
    sleep(1)
  
  #paddle1 loses
  if ball.xcor() < -400:
    # Add scoreboard notice that game i
    ball.reset()
    score2.calculate_score()
    screen.update()
    sleep(1)

screen.exitonclick()
