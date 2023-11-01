COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ALIGMENT ="center"
FONT = ("Courier" , 72 , "normal")
from turtle import Turtle, Screen
import random
class CarManager:

    def __init__(self):

        self.all_car = []

    def create_car(self):
        random_chance = random.randint(1,10)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1 , stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            cord_y = random.randint(-240,240)
            new_car.goto(300,cord_y)
            new_car.setheading(180)
            new_car.showturtle()
            new_car.speed(1)
            self.all_car.append(new_car)
            self.car_speed = STARTING_MOVE_DISTANCE

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)
    def move_cars(self):
        for car in self.all_car:
            car.forward(STARTING_MOVE_DISTANCE)


    def car_stop(self):
        for car in self.all_car:
            car.speed(0)

        popup = Screen()
        popup.setup(600,600)
        info = Turtle()
        info.hideturtle()
        info.write("GAME OVER",False, align=ALIGMENT, font=FONT)