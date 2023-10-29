from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.size = 20
        self.color("red")
        self.shape("circle")
        self.showturtle()
        self.goto(0, 0)

    def ball_movement(self):
        random_angle = random.randint(0, 90)
        self.right(random_angle)
        print(random_angle)
        self.forward(20)


    def wall_detect(self):
        """ Detect a wall collision and create a 90 angle rebound """
        pass

    def paddle_detect(self):
        """Detect ball position in range covered front edge of paddle if not in range call score increse"""
        pass