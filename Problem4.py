from turtle import *

raphael = Turtle()
screen = Screen()

raphael.color("red")
raphael.pensize(5)
raphael.speed(2)
raphael.shape("turtle")

#DRAWING INSTRUCTIONS

def drawTriangle():
	for x in range(3):
		raphael.forward(100)
		raphael.left(120)

drawTriangle()

mainloop()