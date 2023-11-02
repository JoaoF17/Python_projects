from turtle import Turtle
from random import choice, randint

COLORS = ["red", "green", "pink", "purple", "orange", "yellow", "blue"]
STARTING_SPEED = 5
SPEED_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_SPEED

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
          new_car = Turtle("square")
          new_car.shapesize(stretch_wid=1, stretch_len=2)
          new_car.pu()
          new_car.color(choice(COLORS))
          random_y = randint(-220, 250)
          new_car.goto(300, random_y)
          self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
          car.backward(self.speed)
    
    def level_up(self):
      self.speed += SPEED_INCREMENT
