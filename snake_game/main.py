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

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

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
food.make_random_position()

while is_game_On:

    screen.update()
    time.sleep(0.3)
    snake.move(screen)
    snake.check_position()
    if snake.body_collision or snake.wall_collision:
        is_game_On = False
    print(f'FOOD: {food.food_cord}')




screen.exitonclick()
