from turtle import Screen
from paddle import Paddle
from playground import Liner, Counter
from ball import Ball
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
ball_position_y = ball.ycor()
ball_position_x = ball.xcor()
screen.onkey(ball.ball_movement, "g")
while True:
    screen.onkey(right_paddle.paddle_up, "Up")
    screen.onkey(right_paddle.paddle_down, "Down")

    player_1_cnt.score_update()
    player_2_cnt.score_update()
    if ball_position_y in range(-270,270) and ball_position_x in range(-350,350):
        ball.ball_movement()
        screen.update()
        print(f'Ball X:{ball_position_x} / Ball Y:{ball_position_y}')
    if multiPlayer:
        screen.onkey(left_paddle.paddle_up, "w")
        screen.onkey(left_paddle.paddle_down, "s")
    screen.update()
    screen.exitonclick()
