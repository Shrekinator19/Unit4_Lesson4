from turtle import *

marissa = Turtle()
screen = Screen()
screen.bgcolor("yellow")

marissa.color("green")
marissa.pensize(5)
marissa.speed(2)
marissa.shape("turtle")

#DRAWING INSTRUCTIONS

for x in range(8):
	forward(100)
	left(135)

mainloop()