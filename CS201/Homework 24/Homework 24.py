#Homework 24
#Programmer Lauren Cox
#Date of Last Revision 24-3-2016

import turtle

a=turtle.Screen()
b=turtle.Turtle()

infile=open('Homeworkfile24.py','r')
file_contents=infile.readlines()
infile.close()

my_listx=[]
my_listy=[]
for line in file_contents:
    clean_line=line.rstrip()
    line=clean_line.split(',')
    my_listx.append(float(line[0]))
    my_listy.append(float(line[1]))
temp_list=my_listx
temp_list1=my_listy
temp_list.sort()

rx=(temp_list[-1]-temp_list[0])
ry=(temp_list1[-1]-temp_list[0])

b.shape('circle')
b.penup()

for item in range(len(my_listx)):
        b.goto(int((my_listx[item]-temp_list[0])/rx*300),int((my_listy[item]-temp_list1[0])/ry*300))
        b.stamp()
        
    
    
