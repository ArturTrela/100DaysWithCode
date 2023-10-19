from turtle import Turtle , Screen

boot = Turtle()
boot.shape("arrow")
boot.shapesize(1)
boot.color("blue")
boot.pensize(2)
boot.pencolor("red")

for turn in range (0 ,4):
    boot.forward(100)
    boot.right(90)
    turn +=1

my_screen =Screen()
my_screen.canvwidth = 640
my_screen.exitonclick()
