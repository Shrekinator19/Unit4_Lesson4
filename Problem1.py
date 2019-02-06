from turtle import *

fiona = Turtle()
screen = Screen()

fiona.color("grey")
fiona.pensize(6)
fiona.speed(9)
fiona.shape("turtle")

# DRAWING INSTRUCTIONS

fiona.forward(80)
fiona.left(50)
fiona.forward(200)
fiona.right(150)
fiona.forward(50)
fiona.backward(300)

fiona.circle(25)
mainloop()