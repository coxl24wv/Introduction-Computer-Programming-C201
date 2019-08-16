#Homework 27
#Programmer Lauren Cox
#Date of Last Revision 28-4-2016

import turtle
s=0
a=turtle.Screen()
b=turtle.Turtle()

b.penup()
b.goto(-75,-160)
b.pencolor("black")
b.pensize(250)
b.pendown()
b.forward(150)
b.left(90)
b.forward(325)
b.left(90)
b.forward(150)
b.left(90)
b.forward(325)


def key_color_x1():
    s=b.position()
x    b.penup()
    b.shapesize(8)
    b.shape("circle")
    b.pensize(330)
    if s[1]==0:
        b.hideturtle()
        b.goto(0,125)
        b.color("red")
        b.showturtle()
 
    elif s[1]==125:
        b.hideturtle()
        b.goto(0,-125)
        b.color("green")
        b.showturtle()
    else:
        b.hideturtle()
        b.goto(0,0)
        b.color("yellow")
        b.showturtle()    
        
    return


a.onkey(key_color_x1,"x")
a.listen()

a.mainloop()


