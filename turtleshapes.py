import turtle
#for i in range(4):
    #turtle.forward(100)
    #turtle.right(144)

#turtle.forward(100)

###turtle.forward(40)
###turtle.right(90)
####turtle.forward(40)
####turtle.right(45)
####turtle.forward(40)
###turtle.right(100)
#####turtle.forward(40)
######turtle.right(45)
######turtle.forward(40)
#turtle.register_shape("cr7", ((0,0),(0,50),(50,50),(100,25),(50,0),(0,0)))
###turtle.getshapes()
##turtle.shape("cr7")
##turtle.mainloop()
turtle.speed(6900000)
a=0
while (a<360):
    turtle.forward(150)
    turtle.forward(150)
    turtle.right(50)
    turtle.forward(50)
    turtle.forward(150)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    turtle.penup()
    turtle.home()
    a+=1
    turtle.right(a)
    turtle.pendown()
    
turtle.mainloop()
