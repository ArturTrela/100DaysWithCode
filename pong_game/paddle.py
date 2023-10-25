from turtle import Turtle
UPPER_EDGE = 50
LOWER_EDGE = -50

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.showturtle()
        self.goto(350, 0)

    def paddle_up(self):
        pass

    def paddle_down(self):
        pass


