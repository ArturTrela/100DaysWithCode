from turtle import Screen
from paddle import Paddle
from pong_game import paddle

screen =Screen()
screen.bgcolor("Black")
screen.setup(800, 600)
screen.tracer(0)
screen.listen()
screen.title("PONG GAME ")
right_paddle = Paddle()
left_paddle = Paddle()
left_paddle.color("Blue")
left_paddle.goto(-350,0)
multiPlayer = False
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
if multiPlayer:
    screen.onkey(left_paddle.paddle_up, "w")
    screen.onkey(left_paddle.paddle_down, "s")

screen.update()
screen.exitonclick()
