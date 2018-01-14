from turtle import*
import random
import speed
import math


colormode(255)
class circle(Turtle):
	def __init__(self, x, y, dx, dy, radius)
	   Turtle.__init(self)
	   self.shape('circle')
	   self.size(raius/10)
	   self.x=x
	   self.y=y
	   self.dx=dx
	   self.dy=dy
	   self.radius=radius

def move():
	currentx=x
	currenty=y
	self.goto(currentx+self.dx,currenty+self.dy)

my_x=random.randint(-300,100)
my_y=random.randint(-300,100)
my_dx=random.randint(10,15)
my_dy=random.randint(10,15)
circle1=circle(my_x,my_y,my_dx,my_dy,10)


my_x=random.randint(-200,150)
my_y=random.randint(-200,150)
my_dx=random.randint(5,15)
my_dy=random.randint(5,15)
circle2=circle(my_x,my_y,my_dx,my_dy,15)


my_x=random.randint(-130,100)
my_y=random.randint(-130,100)
my_dx=random.randint(5,20)
my_dy=random.randint(5,20)
circle3=circle(my_x,my_y,my_dx,my_dy,10)
while true:
	circle1.move()
	circle2.move()
	circle3.move()
mainloop()









