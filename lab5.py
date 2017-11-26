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



class rectangle(Turtle):
	def __init__(self,hight,width):
		Turtle.__init__(self)
		
		register_shape('carlos' ,(0,0) (0,width) , (hight,width) , (0,hight) , (0,width))
		self.shape('carlos')
		self.setheading(90)
rectangle1=rectangle(100,50)
mainloop()
colormode(255)
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)
class hexagon(Turtle):
	def __init__(self,size):
	  Turtle.__init__(self)
	  self.shapesize(size)
	  # self.speed(speed)
	  self.begin_poly()
	  self.color(red,green,blue)
	  self.begin_fill()
	  for i in range(0,6):
		  self.forward(size)
		  self.left(60)
	  self.end_poly()
	  self.end_fill()
	  register_shape('hexagon', self.get_poly())
	  self.shape('hexagon')
hexegaon1=hexagon(100)
speed(1)
mainloop()