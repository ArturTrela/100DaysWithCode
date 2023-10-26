from turtle import Turtle, Screen
UPPER_EDGE = 50
LOWER_EDGE = -50
PLAYGROUND_LIMIT_UP = 250
PLAYGROUND_LIMIT_DOWN = -250
play_ground = Screen()
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
        if self.ycor() < 240 :
            self.setheading(90)
            self.forward(20)
            play_ground.update()

    def paddle_down(self):
        if self.ycor() > - 240 :
            self.setheading(270)
            self.forward(20)
            play_ground.update()


