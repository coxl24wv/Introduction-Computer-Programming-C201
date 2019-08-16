
# Number One

import turtle

a=turtle.Screen
b=turtle.Turtle

'''c=int(a.numinput('Enter Screen','Enter an positive integer'))

b.penup()
b.goto(0,0)
b.pencolor('red')
b.pendown()
b.shapesize(c,c,0)
b.shape('square')

a.mainloop()'''

# Number Two

#primes

'''import datetime
list_of_primes=[2,3}
number_to_test=5
number_of_primes_wanted=int(input('Which prime do you want?:'))
number_of_primes_in_list=2
start_time=datetime.datetime.now()
prime_list_index=1

while number_of_primes_in_list<number_of_primes_wanted:
    number_is_prime=True

    if list_of_prime[prime_list_index]*list_of[primes
        prime_list_index+=1
    for x in range(1,primes_list_index):
        if number_to_test%list_of_primes[x]==0:
            number_is_prime=False
            break'''







#Homework 21
#Programmer Jeremy Starks
#Date of last revision 25-03-2016
#Purpose: Illustrate creating a menu

file_contents = []

while 1:
    print("1. Read a file called stuff.txt")
    print("2. Save a file called stuff.txt")
    print("3. Add a record to stuff.txt")
    print("4. Delete a record from stuff.txt")
    print("5. Change record in stuff.txt")
    print("6. Sort list in file stuff.txt")
    print("7. Do nothing and end program")

    userchoice = int(input("Choose a number:"))
    
    if userchoice == 1:
        infile = open("stuff.txt")
        file_contents = infile.readlines()
        for i in range (len(file_contents)):
            file_contents[i] = file_contents[i].replace ("\n","")
        infile.close()
        print(file_contents)
    elif userchoice == 2:
        outfile = open("stuff.txt","w")
        for s in file_contents:
            print(s,file = outfile)
        outfile.close()
    elif userchoice == 3:
        newRecord = input("Give me a new record: ")
        file_contents.append(newRecord)
        print(file_contents)
    elif userchoice == 4:
        deleteRecord = input("Give me a record to delete: ")
        file_contents.remove(deleteRecord)
        print(file_contents)
    elif userchoice == 5:
        changeRecord = input("Give me a record to change: ")
        recordPosition = -1
        for i in range(len(file_contents)):
            if file_contents[i] == changeRecord:
                recordPosition = i
                break

        if recordPosition >= 0:
            print("Record found.")
            newRecord = input("Give me the new value of the record: ")
            file_contents[recordPosition] = newRecord
        else:
            print("Record not found.")
        print(file_contents)
    elif userchoice == 6:
        file_contents.sort()
        print(file_contents)
    elif userchoice == 7:
        break
















 #Homework 25
#Programmer Jeremy Starks
#Date of last revision 27-03-2016
#Purpose: Illustrate creating a paint program

import turtle

wn=turtle.Screen()
paint=turtle.Turtle()
paint.shape("triangle")
paint.penup()
#paint.goto(0,0)
paint.pendown()

def pen_up(x,y):            
    #paint.penup()
    paint.goto(x,y)
    return
def pen_down(x,y):
    #paint.pendown()
    change_color(x,y)
    paint.goto(x,y)
    return
def change_color(x,y):
    if x>0:
        if y>0:
            paint.pencolor("blue")
            paint.pensize(30)
            wn.title("Quadrant I")
        else:
            paint.pencolor("orange")
            paint.pensize(10)
            wn.title("Quadrant IV")
    else:
        if y>0:
            paint.pencolor("red")
            paint.pensize(5)
            wn.title("Quadrant II")
        else:
            paint.pencolor("black")
            paint.pensize(20)
            wn.title("Quadrant III")
    return
paint.ondrag(pen_down)#Drags a pen around the screen and draw.
#paint.ondrag(change_color)

#wn.onclick(pen_down)  #picks up the pen and moves it to where you click

wn.mainloop()
   
