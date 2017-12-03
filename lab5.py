from turtle import *
import random

# class Square(Turtle):
#     def __init__(self,size):
#        Turtle.__init__(self)
#        self.shapesize(size)
#        self.shape('square')

#     def random_color(self):
#     	self.color(red,green,blue)
# square1=Square(10)
# square1.random_color()


# mainloop()

                     #extaaaaaaaaaa

colormode(255)
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)
class rectangle(Turtle):
	def __init__(self, height, width):
		Turtle.__init__(self)
		self.color(red,green,blue)
		# self.height(height)
		# self.width(width) 

		
		register_shape('rectangle' ,((0,0) ,(width,0) , (width,height) , (0,height)))
		self.shape('rectangle')
		self.setheading(90)
	# def color_ful(self):
	# 	self.color(red,green,blue)



rectangle1=rectangle(100,50)
# rectangle1(color_ful)
# print(rectangle1)
# bmainloop()





# colormode(255)
# red=random.randint(0,255)
# green=random.randint(0,255)
# blue=random.randint(0,255)
# class hexagon(Turtle):
# 	def __init__(self,size):
# 	  Turtle.__init__(self)
# 	  self.shapesize(size)
# 	  self.speed(1)
# 	  self.begin_poly()
# 	  self.color(red,green,blue)
# 	  self.begin_fill()
# 	  for i in range(0,6):
# 		  self.forward(size)
# 		  self.left(60)
# 	  self.end_poly()
# 	  self.end_fill()
# 	  register_shape('hexagon', self.get_poly())
# 	  self.shape('hexagon')
# hexagon1=hexagon(50)

# mainloop()


#       test      ########

# colormode(255)
# red=random.randint(0,255)
# green=random.randint(0,255)
# blue=random.randint(0,255)
# class rectangle(Turtle):
# 	def __init__(self, height, width):
# 		Turtle.__init__(self)
# 		self.color(red,green,blue)
# 		# self.height(height)
# 		# self.width(width) 


		
# 		register_shape('rectangle' ,((0,0) ,(-width/2,0) , (0,-height/2) , (width/2,height) , (-width,height/2)))
# 		self.shape('rectangle')
# 		self.setheading(90)
# 	# def color_ful(self):
# 	# 	self.color(red,green,blue)


# rectangle1=rectangle(100,50)
# # rectangle1(color_ful)
# # print(rectangle1)
# mainloop()



