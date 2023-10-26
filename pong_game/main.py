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

screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.update()
screen.exitonclick()
