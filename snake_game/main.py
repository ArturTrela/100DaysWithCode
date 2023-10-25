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

"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(600, 600)

screen.bgcolor("black")
screen.title("My snake game ")
screen.tracer(0)

is_game_On = True
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
scoreboard = Scoreboard()


while is_game_On:

    screen.update()
    time.sleep(0.2)
    snake.move(screen)
    snake.check_position()
    if snake.wall_collision:
        is_game_On = False
        scoreboard.game_over()

    if snake.head.distance(food) < 15:
        print(f'Food detect !')
        food.make_random_position()
        snake.extend()
        scoreboard.increase_score()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_On = False
            scoreboard.game_over()

screen.exitonclick()
