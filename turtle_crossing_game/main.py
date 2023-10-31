import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
game_loop =0
car = CarManager()
screen.onkey(player.move, "Up")
scoreboard = Scoreboard()
scoreboard.clear()
scoreboard.goto(-230 , 260)
scoreboard.score_update()
game_is_on = True
play_speed = 0.1
while game_is_on:

    if game_loop % 12 == 0:
        car= CarManager()
    # car.move()
    time.sleep(play_speed)

    if player.onFinish:
        scoreboard.increase_score()
    player.check_finish()
    screen.update()
    car.move()
    game_loop +=1

screen.exitonclick()