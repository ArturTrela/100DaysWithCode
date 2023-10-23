from turtle import Turtle
import random

LEFT_WALL = -300
RIGHT_WALL = 300
TOP_WALL = 300
BOTTOM_WALL = -300

class Food:

    def __init__(self):
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("blue")
        self.food.shapesize(1)
        self.food_cord = ()
        global food_x_cord = self.food_cord[0]
        global food_y_cord = self.food_cord[1]


    def make_random_position(self):

        food_new_x = random.randint(LEFT_WALL, RIGHT_WALL)
        food_new_x = food_new_x - (food_new_x % 20)
        food_new_y = random.randint(BOTTOM_WALL, TOP_WALL )
        food_new_y = food_new_y - (food_new_y % 20)
        self.food.goto(food_new_x,food_new_y)
        self.food_cord = (food_new_x, food_new_y)
        return self.food_cord, food_new_x,food_new_y

