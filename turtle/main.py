import turtle
from turtle import Turtle, Screen
import random
boot = Turtle()
boot.shape("classic")
boot.shapesize(1)
boot.color("black")
boot.pensize(2)
boot.pencolor("OrangeRed1")


#
#
# """Making a square"""
#
# for turn in range (0 ,4):
#     boot.pendown()
#     boot.forward(100)
#     boot.right(90)
#     turn +=1
#     boot.penup()
#
# """Making a dashed line """
# boot.setpos(30,50)
# for _ in range(10):
#     boot.pendown()
#     boot.forward(10)
#     boot.penup()
#     boot.forward(10)

# """Make a different shapes"""
# angle = 3
# lines = 3
#
#
# def draw_shape(kat, bok):
#
#     for x in range(bok):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         boot.pendown()
#         turtle.colormode(255)
#         boot.pencolor((r, g, b))
#         boot.forward(100)
#         boot.right(360 / kat)
#
#
# while lines < 9:
#     draw_shape(angle, lines)
#     angle += 1
#     lines += 1




"""Making a random Walk with random colors """

def random_walk():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    boot.speed(0)
    boot.pensize(4)
    angle = [0,90,180,270]
    boot.pendown()
    turtle.colormode(255)
    boot.pencolor((r, g, b))
    boot.forward(40)
    boot.setheading(random.choice(angle))

for a in range (200):
    random_walk()

my_screen = Screen()
my_screen.exitonclick()

