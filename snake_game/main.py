"""
DAY 1 requirement :
1. create a snake body
2. Make a snake
3. Control the snake
"""

"""  
DAY 2 requirement :
1. Detect collision with food
2. Create a scoreboard
3. Detect collision with wall
4. Detect collision with tail
"""

from turtle import Turtle, Screen

is_game_On = True
long_body = []
snake = Turtle(shape="square")

snake.penup()
snake.shapesize(1)

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")


for body_index in range(0,3):
    snake = Turtle(shape="square")
    snake.shapesize(1)
    snake.pencolor("white")
    snake.fillcolor("white")
    snake.setx(-20*body_index)
    long_body.append(snake)
    print(long_body)
def move_upward():
    snake.forward(10)
    snake.setheading(90)




def move_downward():
    snake.setheading(270)
    snake.forward(10)


def move_left():
    snake.setheading(180)
    snake.forward(10)

def move_right():
    snake.setheading(0)
    snake.forward(10)


while is_game_On:
    snake_x_cord = snake.xcor()
    snake_y_cord = snake.ycor()
    # snake.setx(snake_x_cord + 10)


    screen.listen()
    screen.onkey(move_upward,"w")
    screen.onkey(move_downward,"s")
    screen.onkey(move_left,"a")
    screen.onkey(move_right,"d")

    screen.exitonclick()



