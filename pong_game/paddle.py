from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.setheading(90)
        self.showturtle()
        self.goto(350, 0)

    def paddle_up(self):
        if self.ycor() < 250 :
            self.setheading(90)
            self.forward(20)
            position = (self.ycor())
            print(position)


    def paddle_down(self):
        if self.ycor() > - 250:
            self.setheading(270)
            self.forward(20)
            position = (self.ycor())
            print(position)


