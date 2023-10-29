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
        y_cord = self.ycor()
        x_cord = self.xcor()
        random_angle = random.randint(0, 90)
        self.right(random_angle)
        if y_cord < 270 or y_cord > - 270:
            self.forward(50)
        print(random_angle)




    def wall_detect(self):
        """ Detect a wall collision and create a 90 angle rebound """
        pass

    def paddle_detect(self):
        """Detect ball position in range covered front edge of paddle if not in range call score increse"""
        pass