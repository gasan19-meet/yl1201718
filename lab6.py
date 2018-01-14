
from turtle import*  
import random
import math
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape('circle')
		self.shapesize(radius/10)
		self.color(color)
		self.speed(speed)
		self.radius=radius

ball_1=Ball(60,'blue',10)
# ball_1.goto(0,0)
ball_2=Ball(50,'green',12)
ball_2.goto(100,0)

# penup()

# ball_2.goto(0,0)


def check_collisions(ball_1,ball_2):
	if ball_1.radius + ball_2.radius > math.sqrt(math.pow((ball_2.xcor()-ball_1.xcor()),2)+math.pow((ball_2.ycor()-ball_1.ycor()),2)):
		print('its collision szn boys')
	else:
		
		print('safe:no collision')
# def edge_case(ball_1,ball_2):
# 	if ball_1.radius + ball_2.radius == math.sqrt(math.pow((ball_1.xcor()-ball_2.xcor()),2)+math.pow((ball_1.ycor()-ball_2.ycor()),2)):
# 		print('edgin buddy')
# def ball_size(ball_1,ball_2):

# 	if ball_1.radius<ball_2.radius:
	
# 		print('ball_2 is bigger than ball_1')
# 	elif ball_2.radius<ball_1.radius:
# 		print('ball_1 is bigger than ball_1')

check_collisions(ball_1,ball_2)
# edge_case(ball_1,ball_2)
# ball_size(ball_1,ball_2)
mainloop()