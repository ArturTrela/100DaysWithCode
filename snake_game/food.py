from turtle import Turtle
import random

LEFT_WALL = -300
RIGHT_WALL = 300
TOP_WALL = 300
BOTTOM_WALL = -300

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("blue")
        self.shapesize(stretch_wid=10, stretch_len=10)
        self.food_cord = []

    def make_random_position(self):

        food_new_x = random.randint(LEFT_WALL, RIGHT_WALL)
        food_new_x = food_new_x - (food_new_x % 20)
        food_new_y = random.randint(BOTTOM_WALL, TOP_WALL )
        food_new_y = food_new_y - (food_new_y % 20)
        self.food.goto(food_new_x,food_new_y)
        self.food_cord = [food_new_x, food_new_y]
        return self.food_cord, food_new_x,food_new_y

