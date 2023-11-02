from turtle import Turtle

ALIGMENT = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.score = 0
        self.goto(0, 250)
        self.color("White")
        self.score_update()

    def score_update(self):
        self.write(f'Score = {self.score} | Last High Score : {self.high_score}', False, align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            score_to_file = self.high_score
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(f'{score_to_file}')
            high_score_file.close()
        self.score = 0
        self.clear()
        self.score_update()

    def last_high_score(self):
        high_score_file = open("high_score.txt", "r")
        lines = high_score_file.readlines()

        # print(lines)
        for line in lines:
            print(line)
        if len(lines) > 0:
            score_from_file = lines[0]
            self.high_score = score_from_file
        else:
            pass
        self.score_update()
        high_score_file.close()