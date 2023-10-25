from turtle import Turtle
import random

LEFT_EDGE = -250
RIGHT_EDGE = 250
TOP_EDGE = 250
BOTTOM_EDGE = -250

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

        self.make_random_position()

    def make_random_position(self):

        food_new_x = round(random.randint(LEFT_EDGE, RIGHT_EDGE))
        food_new_x = food_new_x - (food_new_x % 20)
        food_new_y = round(random.randint(BOTTOM_EDGE, TOP_EDGE))
        food_new_y = food_new_y - (food_new_y % 20)
        self.goto(food_new_x, food_new_y)
        return food_new_x, food_new_y

