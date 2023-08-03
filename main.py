import turtle
from turtle import Turtle, Screen
import random
import colorgram

"""Creating an rgb list from an image using 'colorgram' package """
colors = colorgram.extract("image.jpg", 100)
all_colors = []
color_tuple = ()

for i in range(len(colors)):
    color_tuple = ()
    color_tuple += colors[i].rgb
    all_colors.append(color_tuple)

print(all_colors)

color_list = [(249, 248, 248), (232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

"""Implementing the Hirst Painting using Turtle """
point = Turtle()
turtle.colormode(255)

position_y = 0
for i in range(1, 101):
    point.hideturtle()
    point.dot(20, random.choice(color_list))
    point.penup()
    point.forward(50)
    if i % 10 == 0:
        position_y += 50
        point.goto(0, position_y)

screen = Screen()
screen.exitonclick()

