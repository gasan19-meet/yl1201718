from  turtle import*
import turtle
import time
import random
from ball4 import circle
import math


intro = turtle.clone()
intro.ht()
intro.pu()
intro.goto(-150,150)
intro.write('Instructions:',move=True ,align='left' , font=('Arial',55,'normal'))
intro.goto(-300,70)
intro.write('You are the black ball, move the mouse to move your ball.',move=True, font=('Arial',17,'normal'))
intro.goto(-300,20)
intro.write('Eat balls that are smaller than you by bumping into them.',move=True,font=('Arial',17,'normal'))
intro.goto(-300,-30)
intro.write('If you bump into a bigger ball you will LOSE.',move=True,font=('Arial',17,'normal'))
intro.goto(-320,-80)
intro.write('BEWARE if you bump into the blue ball you will LOSE A POINT.',move=True,font=('Arial',17,'normal'))
# intro.goto(-240,-80)
# write('beware if you hit the blue ball you will lose one point and your ball will get smaller.',move=True,font=('Arial',17,'normal'))
intro.goto(-150,-180)
intro.write('HAVE FUN',move=True,font=('Arial',55,'normal'))
time.sleep(2)
intro.clear()
pu()
write('3',move=True,align='center',font=('Arial',70,'normal'))
time.sleep(2)
clear()
pu()
write('2',move=True,align='center',font=('Arial',70,'normal'))
time.sleep(1)
clear()
pu()
write('1',move=True,align='center',font=('Arial',70,'normal'))
clear()
time.sleep(1)


tracer(0)
hideturtle()
RUNNING=True 
SLEEPING=0.0077
SCREEN_WIDTH=getcanvas().winfo_width()/2
SCREEN_HEIGHT= getcanvas().winfo_height()/2
score=0
shark_ball=circle(30,20,2,5,15,'blue')
# intro()



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
	shark_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
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
				pu()
				turtle.goto(0,0)
				write('GAME OVER',align='center', font=("Arial", 60, "normal"))
				print('GAME OVER')
				return False
			elif my_ball.radius>other_ball.radius:
				my_ball.radius+=1
				global score
				score +=1
				clear()
				pu()
				goto(-250,150)
				write(score,align='right', font=('Arial',48,'normal'))
				write("",align='center', font=('Arial',20,'normal'))
				my_ball.shapesize(my_ball.radius/10)
				other_ball.goto(screen_xpos,screen_ypos)
				other_ball.dx=ball_dx
				other_ball.dy=ball_dy
				other_ball.radius=ball_radius
				other_ball.shapesize(other_ball.radius/10)
	
	if collide(shark_ball,my_ball)==True:
		print("collided")
		clear()
		global score
		score-=1
		pu()
		goto(-250,150)
		write(score,align='right', font=('Arial',48,'normal'))
		pu()
		turtle.goto(0,0)
		# if my_ball.radius<other_ball.radius:
		# 		write('GAME OVER',align='center', font=("Arial", 60, "normal"))
		# 		print('GAME OVER')

		# write('GAME OVER',align='center', font=("Arial", 60, "normal"))

		my_ball.radius-=1
		shark_ball.goto(screen_xpos,screen_ypos)
		shark_ball.dx=ball_dx
		shark_ball.dy=ball_dy
		shark_ball.radius=15
		shark_ball.shapesize(shark_ball.radius/10)
	return True

def encourage():
	global score
	if score==5:
		turtle.pu()
		goto(-250,0)
		write('AYYYYY Not bad ',move=True,font=('Arial',48,'normal'))
	if score==10:
		turtle.pu()
		goto(-250,0)
		write('pretty good',move=True,font=('Arial',48,'normal'))
	if score==15:
		turtle.pu()
		goto(-250,0)
		write('impressive',move=True,font=('Arial',48,'normal'))
	if score==20:
		turtle.pu()
		goto(-250,0)
		write('incredible work',move=True,font=('Arial',48,'normal'))
	if score==25:
		turtle.pu()
		goto(-250,0)
		write('AMAZING',move=True,font=('Arial',48,'normal'))
	if score==30:
		turtle.pu()
		goto(-250,0)
		write('youre a PRO buddy',move=True,font=('Arial',48,'normal'))

def win():
	# if my_ball.radius==100
	if score==15 or my_ball.radius>SCREEN_WIDTH/2:
		turtle.pu()
		goto(-175,0)
		write('YOU WIN!!!!!!',move=True,font=('Arial',60,'normal'))
		clear()
		write('CONGRATS',move=True,font=('Arial',60,'normal'))
		RUNNING=False



		# clear()

			

def movearound(event):
	my_ball.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)
getcanvas().bind("<Motion>", movearound)
getscreen().listen()

		
# my_score=0

# def score():
# 	if check_myball_collision()==True:
# 		new_score=my_score+1
# 		write('my score:new_score',align='left',font=('arial',20,'normal'))


# for i in range(5000000):
# 	move_all_balls()
# 	check_all_balls_collision()
# 	getscreen().update()




while RUNNING==True:
	# write('3',move=True,align='center',font=('Arial',70,'normal'))
	# time.sleep(1)
	# clear()
	# write('2',move=True,align='center',font=('Arial',70,'normal'))
	# time.sleep(1)
	# clear()
	# write('1',move=True,align='center',font=('Arial',70,'normal'))
	# clear()
	# time.sleep(1)


	if SCREEN_WIDTH!=getcanvas().winfo_width()/2:
		SCREEN_WIDTH=getcanvas().winfo_width()/2
	if SCREEN_HEIGHT!=getcanvas().winfo_height()/2:
		SCREEN_HEIGHT=getcanvas().winfo_height()/2

	move_all_balls()
	check_all_balls_collision()
	encourage()
	win()
	my_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	RUNNING=check_myball_collision()
	# if score<-10:
	# 	write('GAME OVER',align='center', font=("Arial", 60, "normal"))

	# # score()
	# print('hi')
	getscreen().update()
	time.sleep(SLEEPING)
# pu()
# goto(-250,150)
# write(score,align='right', font=('Arial',48,'normal'))



getscreen().update()
mainloop()
