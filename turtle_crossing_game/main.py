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
car_menager = CarManager()
screen.onkey(player.move, "Up")
scoreboard = Scoreboard()
scoreboard.clear()
scoreboard.goto(-230 , 260)
scoreboard.score_update()
game_is_on = True
play_speed = 0.1
while game_is_on:

    time.sleep(play_speed)
    screen.update()
    car_menager.create_car()
    car_menager.move_cars()


    if player.onFinish:
        scoreboard.increase_score()
    player.check_finish()

    game_loop += 1
    print(game_loop)
screen.exitonclick()