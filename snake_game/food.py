from turtle import Turtle
import random

LEFT_WALL = -300
RIGHT_WALL = 300
TOP_WALL = 300
BOTTOM_WALL = -300

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

        food_new_x = round(random.randint(LEFT_WALL, RIGHT_WALL))
        food_new_x = food_new_x - (food_new_x % 20)
        food_new_y = round(random.randint(BOTTOM_WALL, TOP_WALL))
        food_new_y = food_new_y - (food_new_y % 20)
        self.goto(food_new_x, food_new_y)
        return food_new_x, food_new_y

