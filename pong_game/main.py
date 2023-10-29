from turtle import Screen
from paddle import Paddle
from playground import Liner, Counter
from ball import Ball, play

screen = Screen()
screen.bgcolor("Black")
screen.setup(800, 600)
screen.tracer(0)
screen.listen()
screen.title("PONG GAME ")
right_paddle = Paddle()
left_paddle = Paddle()
left_paddle.color("Blue")
left_paddle.goto(-350,0)
new_line = Liner()
multiPlayer = False
new_line.make_line()
new_line.make_playfield()
player_1_cnt = Counter()
player_2_cnt = Counter()
player_1_cnt.goto(50,260)
player_2_cnt.goto(-50,260)
player_2_cnt.clear()
player_1_cnt.clear()
ball = Ball()

is_game_On = True


while is_game_On:
    screen.onkey(right_paddle.paddle_up, "Up")
    screen.onkey(right_paddle.paddle_down, "Down")
    ball.ball_movement()
    play.update()
    player_1_cnt.score_update()
    player_2_cnt.score_update()

    if multiPlayer:
        screen.onkey(left_paddle.paddle_up, "w")
        screen.onkey(left_paddle.paddle_down, "s")



    ball.wall_detect()
    screen.update()
    screen.exitonclick()
