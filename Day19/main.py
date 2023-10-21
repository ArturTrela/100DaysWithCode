from turtle import Turtle,Screen

johny = Turtle()
screen = Screen()


def move_fwd():
    johny.setheading(0)
    johny.forward(10)

def move_bwd():
    johny.setheading(-180)
    johny.backward(-10)

def move_right():
    johny.setheading(90)
    johny.forward(10)

def move_left():
    johny.setheading(-90)
    johny.forward(10)



screen.listen()
screen.onkey(move_fwd,"w")
screen.onkey(move_bwd,"s")
screen.onkey(move_left , "a")
screen.onkey(move_right,"d")
screen.exitonclick()