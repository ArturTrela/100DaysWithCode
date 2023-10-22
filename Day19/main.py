from turtle import Turtle, Screen

johny = Turtle()
screen = Screen()


def move_fwd():
    johny.forward(10)


def move_bwd():
    johny.backward(10)


def move_right():
    new_heading = johny.heading() + 10
    johny.setheading(new_heading)


def move_left():
    new_heading_left = johny.heading()-10
    johny.setheading(new_heading_left)


def clear():
    screen.reset()
    johny.home()
    """alternative clean screen method"""
    # johny.clear()


screen.listen()
screen.onkey(move_fwd, "w")
screen.onkey(move_bwd, "s")
screen.onkey(move_left, "d")
screen.onkey(move_right, "a")
screen.onkey(clear, "c")
screen.exitonclick()
