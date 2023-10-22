import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Who's WIN", "Type color of winner red / orange / pink / green / blue / purple")
all_turtles = []
colors = ["red", "orange", "pink", "green", "blue", "purple"]
y_position = (-125, -75, -25, 25, 75, 125)
if user_bet:
    is_race_on = True


def player_creator():
    """Creating players"""
    for turtle_index in range(0, 6):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.setposition(-230, (y_position[turtle_index]))
        all_turtles.append(new_turtle)


player_creator()

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.color()
            winner_color = winner_color[0]
            is_race_on = False
            if winner_color == user_bet:
                print(f'You WIN . {winner_color} turtle is winner')
            else:
                print(f'You Lose !{winner_color} turtle was faster')

        pointer_turtles = random.randint(0, len(all_turtles) - 1)
        rand_dist = random.randint(0, 10)
        all_turtles[pointer_turtles].forward(rand_dist)


screen.exitonclick()
