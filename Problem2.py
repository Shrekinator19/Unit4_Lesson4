from turtle import *

jake = Turtle()
screen = Screen()

jake.color("grey")
jake.pensize(6)
jake.speed(9)
jake.shape("turtle")

# DRAWING INSTRUCTIONS
for x in range(4):
	jake.forward(100)
	jake.left(90)

mainloop()