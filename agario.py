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
for i in range(0,1320):
	screen_xpos=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	screen_ypos=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
	ball_dx=random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	ball_dy=random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	ball_radius=random.randint(int(MINIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
	new_ball=circle(screen_xpos,screen_ypos,ball_dx,ball_dy,ball_radius)
print(new_ball)
BALLS.append(new_ball)
mainloop()