# from colorgram import extract

# colors = extract('image.jpeg', 64)

# all_colors = []

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   all_colors.append(new_color)

# print(all_colors)

from turtle import Turtle, Screen, colormode
from random import choice

tim = Turtle()
colormode(255)
tim.home()

color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]

tim.speed("fastest")
tim.pu()
tim.setpos(-250, -250)

x = -250

for _ in range(10):
  for _ in range(10):
    tim.dot(20, choice(color_list))
    tim.fd(50)
  
  x += 50  
  tim.setpos(-250, x)

screen = Screen()
screen.exitonclick()