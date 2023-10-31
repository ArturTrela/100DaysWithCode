from turtle import Turtle, Screen
import random
import time

play = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.size = 20
        self.color("white")
        self.shape("circle")
        self.showturtle()
        self.penup()
        self.goto(0, 0)

    def ball_movement(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        play.update()

    def wall_detect(self):
        """ Detect a wall collision and create a 90 angle rebound """
        if int(self.ycor()) == -270 or self.ycor() == 270:
            print("wall detect method")

    def paddle_detect(self):
        """Detect ball position in range covered front edge of paddle if not in range call score increse"""
        pass
