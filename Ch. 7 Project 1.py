import turtle
from math import pi
def draw_circle(myTurtle, x, y, radius):
    myTurtle.penup()
    myTurtle.setposition(x, y-radius) # move to the position x,y-radius where x ,y will be center
    myTurtle.pendown()
    for i in range(120):
        myTurtle.circle(radius, 3)
    turtle.getscreen().mainloop()
    distance_moved = 2.0*pi*radius/120.0
    return distance_moved

myTurtle = turtle.Turtle()
distance = draw_circle(myTurtle, 200,200 ,50)
print(distance)
