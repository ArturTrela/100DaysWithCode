from turtle import Turtle

import food

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LEFT_WALL = -300
RIGHT_WALL = 300
TOP_WALL = 300
BOTTOM_WALL = -300


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.creating_snake()
        self.head = self.segments[0]
        self.body_collision = False
        self.wall_collision = False
        self.food_collision = False
        self.head_x_cord = self.head.xcor()
        self.head_y_cord = self.head.ycor()

    def creating_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.speed(10)
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self, screen):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.body_collision = True

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            self.body_collision = True

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            self.body_collision = True

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            self.body_collision = True

    def check_position(self):
        act_x_pos = (self.head.xcor())
        act_y_pos = (self.head.ycor())


        if act_x_pos <= LEFT_WALL or act_x_pos >= RIGHT_WALL or act_y_pos >= TOP_WALL or act_y_pos <= BOTTOM_WALL:
            self.wall_collision = True
            self.hideturtle()


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creating_snake()
        self.head = self.segments[0]
