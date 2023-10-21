from turtle import Turtle, Screen

johny = Turtle()
screen = Screen()


def move_fwd():
    johny.forward(10)


def move_bwd():
    johny.backward(10)


def move_right():
    johny.right(5)


def move_left():
    johny.left(5)


screen.listen()
screen.onkey(move_fwd, "w")
screen.onkey(move_bwd, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(screen.clear, "c")
screen.exitonclick()
