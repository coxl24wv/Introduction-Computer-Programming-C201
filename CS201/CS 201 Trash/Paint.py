#Homework 25
#Programmer Lauren Cox
#Date of last revision 28-3-2016

import turtle

a=turtle.Screen()
b=turtle.Turtle()

b.penup()
b.goto(-300,230)
b.pendown()
b.write("Letter Q = green", font=("Segoe Script","12","bold"))
b.penup()
b.pendown()

b.penup()
b.goto(-150,230)
b.pendown()
b.write("Letter W = gray", font=("Segoe Script","12","bold"))
b.penup()
b.pendown()

b.penup()
b.goto(0,230)
b.pendown()
b.write("Letter E = gold", font=("Segoe Script","12","bold"))
b.penup()
b.pendown()

b.penup()
b.goto(150,230)
b.pendown()
b.write("Letter R = blue", font=("Segoe Script","12","bold"))
b.penup()
b.pendown()

def pen_1():
    b.pensize(10)
    b.pencolor("green")
    return
    
def pen_2():
    b.pensize(5)
    b.pencolor("gray")
    return
    
def pen_3():
    b.pensize(25)
    b.pencolor("gold")
    return
    
def pen_4():
    b.pensize(15)
    b.pencolor("blue")
    return

def pen_5(x,y):
    b.pendown()
    b.goto(x,y)
    return



a.onkey(pen_1,"q")
a.onkey(pen_2,"w")
a.onkey(pen_3,"e")
a.onkey(pen_4,"r")

b.ondrag(pen_5)


a.listen()
a.mainloop()
