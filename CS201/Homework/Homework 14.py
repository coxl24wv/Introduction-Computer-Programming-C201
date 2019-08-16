#Homework 14
# Programmer Lauren Cox
# Date of last revision 4-02-2016

basic_list=[]
name=input('give me a name <Enter> with nothing else stops.')

while name!='':
    basic_list.append(name)
    name=input('Give me a name. <Enter with nothing else stops.')

basic_list.reverse()
print(basic_list)
