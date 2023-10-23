from turtle import Turtle

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
class Snake:

    def __init__(self):
        self.segments = []
        self.creating_snake()
        self.head = self.segments[0]
        self.body_collision = False

    def creating_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.speed(10)
            snake.goto(position)
            self.segments.append(snake)

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
        act_x_pos = round(self.head.xcor())
        act_y_pos = round(self.head.ycor())
        print(f'X: {act_x_pos},Y: {act_y_pos}')

        if act_x_pos == LEFT_WALL or act_x_pos == RIGHT_WALL or act_y_pos == TOP_WALL or act_y_pos == BOTTOM_WALL:
            print("Wall Collision")

        if self.body_collision:
            print("Body Collision")
