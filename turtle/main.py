from turtle import Turtle , Screen

boot = Turtle()
boot.shape("turtle")
boot.shapesize(2)
boot.color("pink")
boot.pensize(2)
boot.pencolor("green")

for turn in range (0 ,4):
    boot.forward(100)
    boot.right(90)
    turn +=1

my_screen =Screen()
my_screen.canvwidth = 640
my_screen.exitonclick()
