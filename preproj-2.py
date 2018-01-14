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
	   self.goto(-300,-300)
	   self.pendown()
	   self.goto(-300,300)
	   self.goto(300,300)
	   self.goto(300,-300)
	   self.goto(-300,-300)
	   self.penup()
	def move(self):
		curentx=self.xcor()
		curenty=self.ycor()
		self.goto(curentx+self.dx, curenty+self.dy)
# 	def another_one(self):
# 		random_x=randint(my_x)
# 		random_y=randint(m_y)
# 		random_dx=randint(my_dx)
# 		random_dy=randint(my_dy)
# 		random_radius=radom.randint(10,20)
# 		circle(random_x,random_y,random_dx,random_dy,random_radius)
# another_one(self)


my_x=random.randint(-300,300)
my_y=random.randint(-300,300)
my_dx=random.randint(1,5)
my_dy=random.randint(1,5)
my_radius=random.randint(10,20)
circle1=circle(my_x,my_y,my_dx,my_dy,my_radius)
print('hi')


my_x=random.randint(-200,250)
my_y=random.randint(-200,250)
my_dx=random.randint(1,5)
my_dy=random.randint(1,5)
my_radius=random.randint(10,20)
circle2=circle(my_x,my_y,my_dx,my_dy,my_radius)
print(circle1)

my_x=random.randint(-330,300)
my_y=random.randint(-330,300)
my_dx=random.randint(1,5)
my_dy=random.randint(1,5)
my_radius=random.randint(10,20)
circle3=circle(my_x,my_y,my_dx,my_dy,my_radius)
my_x=random.randint(-300,300)
my_y = random.randint(-300, 300)
my_dx= random.randint(-10,10)
my_dy=random.randint(-10,10)
my_radius=random.randint(10,20)
circle4=circle(my_x,my_y,my_dx,my_dy,my_radius)
# def another_one(self):
#     random_x=randint(my_x)
#     random_y=randint(my_y)
#     random_dx=randint(my_dx)
#     random_dy=randint(my_dy)
#     random_radius=radom.randint(10,20)
#     circle(random_x,random_y,random_dx,random_dy,random_radius)
# another_one(self)

# while True:
def another_circle():
	my_x=random.randint(-300,300)
	my_y = random.randint(-300, 300)
	my_dx= random.randint(-10,10)
	my_dy=random.randint(-10,10)
	my_radius=random.randint(10,20)
	random_circle=circle(my_x,my_y,my_dx,my_dy,my_radius)
	random_circle.move()
for i in  range (0,1540):
	circle1.move()
#	another_circle()
	circle2.move()
	another_circle()
	random_circle.move()
	
	circle3.move()
	another_circle()
	random_circle.move()
	circle4.move()
	getscreen().update()
	time.sleep(0.04)
	# if x.cor>300,or x.cor<300
	# if y.cor<-300,or y.cor>300
	# circle.

print('carlos')
# print("xcor = ", circle1.xcor)


if 'circle1.xcor'>(300,0):
	circle1.goto(150,100)
	# circle1.move()

mainloop()