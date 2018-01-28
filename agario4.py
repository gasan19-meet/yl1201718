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
			screen_xpos=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
			screen_ypos=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
			ball_dx=random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
			ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
			ball_radius=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
			while ball_dx or ball_dy==0:
				ball_dx=random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				ball_dy=ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
			if collide(ball_a,ball_b)==True:
				collided_radius_a=ball_a.radius
				collided_radius_b=ball_b.radius
				if ball_a.radius>ball_b.radius:
					ball_a.radius+=1
					ball_a.shapesize(ball_a.radius/10)
					ball_b.goto(screen_xpos,screen_ypos)
					ball_b.dx=ball_dx
					ball_b.dy=ball_dy
					ball_b.radius=ball_radius
					ball_b.shapesize(ball_radius/10)


				elif ball_b.radius>ball_a.radius:
					ball_b.radius+=1
					ball_b.shapesize(ball_radius/10)
					ball_a.goto(screen_xpos,screen_ypos)
					ball_a.dx=ball_dx
					ball_a.dy_ball_dy
					ball_a.radius=ball_radius
					ball_a.shapesize(ball_b.radius/10)

def check_myball_collision():
	for ball_a in Balls:
		screen_xpos=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
		screen_ypos=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
		ball_dx=random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
		ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
		ball_radius=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
		if collide(ball_a,my_ball)==True:
			my_ball_radius=my_ball.ball_radius
			other_ball=ball_a.ball_radius
		if my_ball.radius<ball_a.radius:
			return False
		elif my_ball.radius>ball_b.radius:
			my_ball.radius+=1
			# my_ball.shapesize(my_ball.radius/10)
			my_ball.goto(screen_xpos,screen_ypos)
			my_ball.dx=ball_dx
			my_ball.dy_ball_dy
			my_ball.radius=ball_radius
			my_ball.shapesize(ball_b.radius/10)
			
	return True
def movearound(event):
	my_ball.move(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)
getcanvas().bind("<Motion>", movearound)
listen()






move_all_balls()
getscreen().update()
mainloop()