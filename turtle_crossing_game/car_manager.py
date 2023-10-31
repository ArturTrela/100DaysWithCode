COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1 , stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        cord_y = random.randint(-240,240)
        self.goto(280,cord_y)
        self.setheading(180)
        self.showturtle()
        self.speed(1)


    def move(self):
        new_x = self.xcor()-STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

