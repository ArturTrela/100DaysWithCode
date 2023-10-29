from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.size = 10
        self.color("red")
        self.shape("circle")
        self.showturtle()
        self.goto(0, 0)

    def ball_movement(self):
        """Make a random direction move for ball """
        pass

    def wall_detect(self):
        """ Detect a wall collision and create a 90 angle rebound """
        pass

    def paddle_detect(self):
        """Detect ball position in range covered front edge of paddle if not in range call score increse"""
        pass