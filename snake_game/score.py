
from turtle import Turtle
ALIGMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 250)
        self.color("White")
        self.score_update()

    def score_update(self):
        self.write(f'Score = {self.score}', False, align=ALIGMENT, font=FONT)
    def increase_score(self):
        self.score +=1
        self.clear()
        self.score_update()

    def game_over(self):
        self.shape("square")
        self.shapesize(200,200)
        self.color("grey")
        self.showturtle()
        self.goto(0, 0)
        self.color("White")
        self.write(f" GAME OVER.",False, align=ALIGMENT, font=FONT )