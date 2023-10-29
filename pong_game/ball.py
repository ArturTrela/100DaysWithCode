from turtle import Turtle, Screen
import random
import time
play = Screen()

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.size = 20
        self.color("red")
        self.shape("circle")
        self.showturtle()
        self.goto(0, 0)

    def ball_movement(self):
        y_cord = int(self.ycor())
        x_cord = self.xcor()
        random_angle = random.randint(0, 180)
        self.right(random_angle)
        condition_y = int(y_cord) > -230 or int(y_cord) < 230
        condition_x = int(x_cord) > -300 or int(x_cord) < 300

        # for s in range(40):
        #     self.forward(10)
        #     print(random_angle)
        #     play.update()
        #     time.sleep(0.2)
        if condition_x or condition_y:
            for s in range(40):
                self.forward(10)
                y_cord = self.ycor()
                x_cord = self.xcor()
                print(y_cord)
                play.update()
                time.sleep(0.1)
            print('wall detection')




    def wall_detect(self):
        """ Detect a wall collision and create a 90 angle rebound """
        if int(self.ycor()) == -270 or self.ycor() == 270:
            print("wall detect method")

    def paddle_detect(self):
        """Detect ball position in range covered front edge of paddle if not in range call score increse"""
        pass