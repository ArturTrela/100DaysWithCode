# import colorgram as cg
#
# pallet_color = []
# colors = cg.extract('image.jpg',30)
# for x in range(30):
#     color = colors[x].rgb
#     r = color.r
#     g = color.g
#     b = color.b
#     # Make a tuple cause params can't be modified in further
#     final_colors = (r, g, b)
#     pallet_color.append(final_colors)
#
# print(pallet_color)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

'''List of color contains 26 colors'''
# x_axis_column = input(f'How many columns on the picture ? ')
# y_axis_row = input('How many rows on the picture ? ')

# test_values =[
# x_axis_column = 10,
# y_axis_row = 10,
# dot_diameter = 20,
# column_width = 20,
# row_width = 20,
# x_pos = -200,
# y_pos = -240,
# ]

"""Take a parameters from user """
x_axis_column = int(input('How many columns you want ? '))
y_axis_row = int(input('How many rows you want ? '))
dot_diameter = int(input('Tell me a dot diameter : '))
column_width = int(input(' How width of columns you want ? '))
row_width = int(input(' How width of rows you want ? '))
x_pos = int(input(' Please type start pos i "X" axis : (INT) '))
y_pos = int(input(' Please type start pos i "Y" axis : (INT) '))

"""Turtle init parameters"""
boot = Turtle()
boot.color("Black")
boot.pensize(1)
boot.hideturtle()
boot.speed(10)
turtle.colormode(255)
boot.penup()

boot.setposition(x_pos,y_pos)


def pick_color(list):
    return random.choice(list)


def painting_dot(diameter):
    """Make a dot in a row with choice a random color from color list """
    boot.dot(diameter, pick_color(color_list))
    boot.forward(dot_diameter + column_width)

"""Head loop of program contains movement offset's for axis X and Y """
for n in range(1, y_axis_row+1):
    for m in range(x_axis_column):
        painting_dot(dot_diameter)

    boot.setx(x_pos)
    boot.sety(y_pos + (dot_diameter + row_width) * n)

"""Show a screen with dot"""
my_screen = Screen()
my_screen.exitonclick()

