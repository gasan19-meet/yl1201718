from turtle import*
import random
import math
import time



colormode(255)
# tracer(0)
# hideturtle()




class circle(Turtle):
	def __init__(self, x, y, dx, dy, radius, color = None):
	   Turtle.__init__(self)
	   self.shape('circle')
	   self.shapesize(radius/10)
	   self.pu()
	   self.goto(x,y)
	   # self.y=y
	   self.dx=dx
	   self.dy=dy
	   self.radius=radius
	   if color==None:
	   	r = random.randint(0,255)
	   	g = random.randint(0,255)
	   	b = random.randint(0,255)
	   	self.color((r,g,b))

	   else:
	   	self.color(color)
	   	black=colormode(179)
	   # self.goto(-300,-300)
	   # self.pendown()
	   # self.goto(-300,300)
	   # self.goto(300,300)
	   # self.goto(300,-300)
	   # self.goto(-300,-300)
	   # self.pu()
	def move(self,width,height):
		curentx=self.xcor()
		new_x=curentx+self.dx
		curenty=self.ycor()
		new_y=curenty+self.dy
		right_side_ball=new_x + self.radius
		left_side_ball=new_x -self.radius 
		top_side_ball=new_y + self.radius
		bottom_side_ball = new_y - self.radius
		self.goto(new_x,new_y)

		if top_side_ball>=height or bottom_side_ball<=-height:
			self.dy=self.dy*-1
		if right_side_ball>=width or left_side_ball<=-width:
			self.dx= self.dx*-1

# my_ball=circle(100,10,10,10,15)
# for i in range(50):
# 	my_ball.move(300, 300)

# 	def move(self):
# 		curentx=self.xcor()
# 		curenty=self.ycor()
# 		screen_width(-300,300)
# 		if curentx<300:
# 			# circle.right(150)
# 			# circle1.move()
# 			self.goto(curentx+self.dx, curenty+self.dy)
# 		elif circle.right(150)
# 			circle.move()

# # 	def another_one(self):
# # 		random_x=randint(my_x)
# # 		random_y=randint(m_y)
# # 		random_dx=randint(my_dx)
# # 		random_dy=randint(my_dy)
# # 		random_radius=radom.randint(10,20)
# # 		circle(random_x,random_y,random_dx,random_dy,random_radius)
# my_x=random.randint(-300,300)
# my_y = random.randint(-300, 300)
# my_dx= random.randint(-10,10)
# my_dy=random.randint(-10,10)
# my_radius=random.randint(10,20)
# # another_one(self)


# my_x=random.randint(-300,300)
# my_y=random.randint(-300,300)
# my_dx=random.randint(1,5)
# my_dy=random.randint(1,5)
# my_radius=random.randint(10,20)
# circle1=circle(my_x,my_y,my_dx,my_dy,my_radius)
# print('hi')


# my_x=random.randint(-200,250)
# my_y=random.randint(-200,250)
# my_dx=random.randint(1,5)
# my_dy=random.randint(1,5)
# my_radius=random.randint(10,20)
# circle2=circle(my_x,my_y,my_dx,my_dy,my_radius)
# print(circle1)

# my_x=random.randint(-330,300)
# my_y=random.randint(-330,300)
# my_dx=random.randint(1,5)
# my_dy=random.randint(1,5)
# my_radius=random.randint(10,20)
# circle3=circle(my_x,my_y,my_dx,my_dy,my_radius)
# my_x=random.randint(-300,300)
# my_y = random.randint(-300, 300)
# my_dx= random.randint(-10,10)
# my_dy=random.randint(-10,10)
# my_radius=random.randint(10,20)
# circle4=circle(my_x,my_y,my_dx,my_dy,my_radius)
# # def another_one(self):
# #     random_x=randint(my_x)
# #     random_y=randint(my_y)
# #     random_dx=randint(my_dx)
# #     random_dy=randint(my_dy)
# #     random_radius=radom.randint(10,20)
# #     circle(random_x,random_y,random_dx,random_dy,random_radius)
# # another_one(self)

# # # while True:


# circles=[]
# def another_circle():
# 	my_x=random.randint(-300,300)
# 	my_y = random.randint(-300, 300)
# 	my_dx= random.randint(-10,10)
# 	my_dy=random.randint(-10,10)
# 	my_radius=random.randint(10,20)
# 	random_circle=circle(my_x,my_y,my_dx,my_dy,my_radius)
# 	random_circle.move()
# 	circles.append(random_circle)

# for i in  range (0,1540):
# 	circle1.move()
# 	another_circle()
# 	print('sam')
# 	# random_circle.move()
# 	circle2.move()
# 	another_circle()
# 	# random_circle.move()
	
# 	circle3.move()
# 	another_circle()
# 	# random_circle.move()
# 	circle4.move()
# 	another_circle()
# 	# random_circle.move()
# 	getscreen().update()
# 	time.sleep(0.04)
# 	# if x.cor>300,or x.cor<300
# 	# if y.cor<-300,or y.cor>300
# 	# circle.

# print('carlos')
# # print("xcor = ", circle1.xcor)
# print('circle1.xcor')

# if 'circle1.xcor'>300:
# 	circle.right(150)
# 	circle1.move()

# mainloop()


#          write a code that makes a new circle each time a ball leaves the barriers...(make a loop or function) 
# class square(Turtle):
# 	def __init__(self, x, y, dx, dy,, color = None):
# 	   Turtle.__init__(self)
# 	   self.shape('circle')
# 	   self.shapesize(radius/10)
# 	   self.pu()
# 	   self.goto(x,y)
# 	   # self.y=y
# 	   self.dx=dx
# 	   self.dy=dy
# 	   self.radius=radius
# 	   if color==None:
# 	   	r = random.randint(0,255)
# 	   	g = random.randint(0,255)
# 	   	b = random.randint(0,255)
# 	   	self.color((r,g,b))

# 	   else:
# 	   	self.color(color)
# 	   	black=colormode(179)
# 	   # self.goto(-300,-300)
# 	   # self.pendown()
# 	   # self.goto(-300,300)
# 	   # self.goto(300,300)
# 	   # self.goto(300,-300)
# 	   # self.goto(-300,-300)
# 	   # self.pu()
# 	def move(self,width,height):
# 		curentx=self.xcor()
# 		new_x=curentx+self.dx
# 		curenty=self.ycor()
# 		new_y=curenty+self.dy
# 		right_side_ball=new_x + self.radius
# 		left_side_ball=new_x -self.radius 
# 		top_side_ball=new_y + self.radius
# 		bottom_side_ball = new_y - self.radius
# 		self.goto(new_x,new_y)

# 		if top_side_ball>=height or bottom_side_ball<=-height:
# 			self.dy=self.dy*-1
# 		if right_side_ball>=width or left_side_ball<=-width:
# 			self.dx= self.dx*-1
