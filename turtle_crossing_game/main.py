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
    player.check_finish()
    if player.onFinish:
        scoreboard.increase_score()
        car_menager.level_up()
        player.onFinish = False

    # Detect collision with cars
    for car in car_menager.all_car:
        if player.distance(car) < 20:
            car_menager.car_stop()
            game_is_on = False

    game_loop += 1

screen.exitonclick()