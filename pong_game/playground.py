from turtle import Turtle, Screen

ALIGMENT = "center"
FONT = ("Times New Roman", 24, "normal")


class Liner(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.goto(0, -350)

    def make_line(self):
        print(self.ycor())
        for step in range(10):
            self.pendown()
            self.setheading(90)
            self.forward(50)
            self.penup()
            self.forward(20)
            step += 1
            print(self.ycor())

    def make_court(self):
        self.pencolor("Orange")
        self.pensize(2)
        self.penup()
        self.goto(-370, 250)
        self.pendown()
        self.setheading(0)
        self.forward(740)
        self.setheading(270)
        self.forward(500)
        self.setheading(180)
        self.forward(740)
        self.setheading(90)
        self.forward(500)
        self.penup()


class Counter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

        self.color("White")
        self.score_update()

    def score_update(self):
        self.write(f' {self.score}', False, align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()
