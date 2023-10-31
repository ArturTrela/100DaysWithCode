FONT = ("Courier", 12, "normal")
ALIGMENT = "center"
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("Black")
        self.score_update()

    def score_update(self):
        self.write(f'Level :  {self.score}', False, align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()
