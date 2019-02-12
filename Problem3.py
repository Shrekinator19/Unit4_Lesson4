from turtle import *

kevin = Turtle()
screen = Screen()

kevin.color("orange")
kevin.pensize(5)
kevin.speed(2)
kevin.shape("turtle")

#DRAWING INSTRUCTIONS

for x in range(6):
	forward(100)
	left(60)

mainloop()