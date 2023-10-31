import time
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
left_paddle.goto(-350,0)

multiPlayer = True
# new_line.make_line()
# new_line.make_playfield()
player_1_cnt = Counter()
player_2_cnt = Counter()
player_1_cnt.goto(50,240)
player_2_cnt.goto(-50,240)
player_2_cnt.clear()
player_1_cnt.clear()
ball = Ball()
player_1_cnt.score_update()
player_2_cnt.score_update()

screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")
is_game_On = True

while is_game_On:
    time.sleep(ball.speed)
    screen.update()
    ball.ball_movement()
    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() <-380:
        player_1_cnt.increase_score()
        ball.reset_position()

    if ball.xcor() > 380:
        player_2_cnt.increase_score()
        ball.reset_position()


screen.exitonclick()
