from turtle import*
import random
import math
import time



colormode(255)
tracer(0)
hideturtle()




class circle(Turtle):
	def __init__(self, x, y, dx, dy, radius):
	   Turtle.__init__(self)
	   self.shape('circle')
	   self.shapesize(radius/10)
	   self.pu()
	   self.goto(x,y)
	   # self.y=y
	   self.dx=dx
	   self.dy=dy
	   self.radius=radius
	   r = random.randint(0,255)
	   g = random.randint(0,255)
	   b = random.randint(0,255)
	   self.color(r,g,b)
	def move():
		curentx=self.xcor()
		curenty=self.ycor()
		self.goto(curentx+self.dx,curenty+self.dy)

my_x=random.randint(-300,300)
my_y=random.randint(-300,300)
my_dx=random.randint(1,5)
my_dy=random.randint(1,5)
circle1=circle(my_x,my_y,my_dx,my_dy,10)


my_x=random.randint(-200,250)
my_y=random.randint(-200,250)
my_dx=random.randint(1,5)
my_dy=random.randint(1,5)
circle2=circle(my_x,my_y,my_dx,my_dy,15)


my_x=random.randint(-430,400)
my_y=random.randint(-430,400)
my_dx=random.randint(1,5)
my_dy=random.randint(1,5)
circle3=circle(my_x,my_y,my_dx,my_dy,10)
while True:
	circle1.move()
	circle2.move()
	circle3.move()
	getscreen().update()
	time.sleep(0.04)
mainloop()









