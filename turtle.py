"""Intro into OOP learn to using build method and give an argument for object creating from Class"""
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.shapesize(2)
# timmy.color("pink")
# timmy.pensize(2)
# timmy.pencolor("green")
# timmy.forward(100)
# timmy.tiltangle(-90)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Snorlaqs","Charizard"])
table.add_column("Pokemon type", ["Electric","Water","Fire"])
table.align = "l"
print(table)