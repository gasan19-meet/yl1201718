from turtle import turtle
class Square (turtle):
    def__init__(self,size):
       turtle.__init__(self)
       self.shapesize(size)
       self.shape('square')
    def random_color(self,color):
    	self.color('green')
square1=square(size=10)
print(square1)
