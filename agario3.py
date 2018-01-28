from  turtle import*
import time
import random
from ball4 import circle
tracer(0)
hideturtle()
RUNNING=True 
SLEEPING=0.0077
SCREEN_WIDTH=getcanvas().winfo_width()/2
SCREEN_HEIGHT= getcanvas().winfo_height()/2

my_ball=circle(100,10,10,10,15)
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
for i in range (NUMBER_OF_BALLS):
	screen_xpos=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	screen_ypos=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
	ball_dx=random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	ball_radius=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	new_ball=circle(screen_xpos,screen_ypos,ball_dx,ball_dy,ball_radius)
	BALLS.append(new_ball)
def move_all_balls():
	for i in range (NUMBER_OF_BALLS):
		new_ball.move(-300,300)
def collide(ball_1,ball_2):
	if ball_1==ball_2:
		return False
	if ball_1.radius + ball_2.radius > math.sqrt(math.pow((ball_2.xcor()-ball_1.xcor()),2)+math.pow((ball_2.ycor()-ball_1.ycor()),2)):
			return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				collided_radius_a=ball_a.ball_radius
				collid
				ed_radius_b=ball_b.ball_radius
		if ball_a>ball_b:
			collided_radius_a+=1
			while ball_dx or ball_dy>0:
				ball_b=circle(screen_xpos,screen_ypos,ball_dx,ball_dy,ball_radius)
		elif ball_b>ball_a:
			collided_radius_b+=1
			while ball_dx or ball_dy>0:
				ball_a=circle(screen_xpos,screen_ypos,ball_dx,ball_dy,ball_radius)
def check_myball_collision():
	for my_ball in Balls:
		if collide(my_ball,Balls)==True:
			my_ball_radius=my_ball.ball_radius
			other_ball=ball_b.ball_radius
		if my_ball<ball_b:
			check_myball_collision=False
		elif my_ball>ball_b:
			my_ball+=1
			ball_b=circle(screen_xpos,screen_ypos,ball_dx,ball_dy,ball_radius)




getscreen().update()
mainloop()