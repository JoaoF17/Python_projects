from turtle import Screen
from time import sleep, time
from random import randint
from frog import Frog
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Frogger Cross Roads")
screen.tracer(0)

frog = Frog()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(frog.move_up, "Up")
screen.onkey(frog.move_down, "Down")


game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move()
    
    #Detect collision with the cars
    for car in car_manager.all_cars:
      if car.distance(frog) < 10:
        game_on = False
        scoreboard.game_over()

    # Keep track of the score
    if frog.ycor() > 260:
        frog.frog_reset()
        scoreboard.calculate_level()
        car_manager.level_up()




screen.exitonclick()
