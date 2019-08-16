# Homework 23
# Programmer Lauren Cox
# Date of last revision 22-03-2016

import turtle

a=turtle.Screen()
b=turtle.Turtle()

def move_up_b():
    b.setheading(90)
    b.forward(5)
    return
def move_left_b():
    b.setheading(180)
    b.forward(5)
    return
def move_down_b():
    b.setheading(270)
    b.forward(5)
    return
def move_right_b():
    b.setheading(0)
    b.forward(5)
    return

a.onkey(move_up_b,"w")
a.onkey(move_left_b,"a")
a.onkey(move_down_b,"s")
a.onkey(move_right_b,"d")
a.listen()
a.mainloop()
