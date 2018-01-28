from  turtle import*
import time
import random
from ball4 import circle
import math
tracer(0)
hideturtle()
RUNNING=True 
SLEEPING=0.0077
SCREEN_WIDTH=getcanvas().winfo_width()/2
SCREEN_HEIGHT= getcanvas().winfo_height()/2

my_ball=circle(100,10,0,0,20,'black')
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=30
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
	for new_ball in BALLS:
		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
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
				ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
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
					ball_b.shapesize(ball_b.radius/10)

					ball_a.goto(screen_xpos,screen_ypos)
					ball_a.dx=ball_dx
					ball_a.dy=ball_dy
					ball_a.radius=ball_radius
					ball_a.shapesize(ball_a.radius/10)

def check_myball_collision():
	for other_ball in BALLS:
		screen_xpos=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
		screen_ypos=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
		ball_dx=random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
		ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
		ball_radius=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
		if collide(other_ball,my_ball)==True:
			my_ball_radius=my_ball.radius
			other_ball_radius=other_ball.radius
			if my_ball.radius<other_ball.radius:
				write('GAME OVER',align='center', font=("Arial", 60, "normal"))
				print('GAME OVER')
				return False
			elif my_ball.radius>other_ball.radius:
				my_ball.radius+=1
				my_ball.shapesize(my_ball.radius/10)
				other_ball.goto(screen_xpos,screen_ypos)
				other_ball.dx=ball_dx
				other_ball.dy=ball_dy
				other_ball.radius=ball_radius
				other_ball.shapesize(other_ball.radius/10)
			
	return True
def movearound(event):
	my_ball.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)
getcanvas().bind("<Motion>", movearound)
getscreen().listen()

for i in range(5000000):
	move_all_balls()
	getscreen().update()

# while RUNNING==True:
# 	if SCREEN_WIDTH!=getcanvas().winfo_width()/2:
# 		SCREEN_WIDTH=getcanvas().winfo_width()/2
# 	if SCREEN_HEIGHT!=getcanvas().winfo_height()/2:
# 		SCREEN_HEIGHT=getcanvas().winfo_height()/2
# 	move_all_balls()
# 	check_all_balls_collision()
# 	my_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
# 	RUNNING=check_myball_collision()
# 	getscreen().update()
# 	time.sleep(SLEEPING)



# getscreen().update()
mainloop()