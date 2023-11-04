from turtle import Turtle


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        x_cor = self.xcor()
        y_cor = self.ycor()

