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
        self.step_y = 10
        self.step_x = 10
        self.speed = 0.1

    def ball_movement(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)
        play.update()

    def bounce(self, ):
        """ Detect a wall collision and rebound """
        self.step_y *= -1
        new_y = self.ycor() + self.step_y
        new_x = self.xcor() + self.step_x
        self.goto(new_x, new_y)

    def paddle_bounce(self):
        """Detect ball position in range covered front edge of paddle if not in range call score increse"""
        self.step_x *= -1
        new_y = self.ycor() + self.step_y
        new_x = self.xcor() + self.step_x
        self.goto(new_x, new_y)
        self.speed = self.speed * 0.9

    def reset_position(self):
        self.paddle_bounce()
        self.goto(0, 0)
        self.speed = 0.1