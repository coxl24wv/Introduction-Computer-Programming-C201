#Homework 13
# Programmer Lauren Cox
# Date of last revision 1-3-2016

basic_list1=[]
name=input('give me a name <Enter> with nothing else stops.')

while name!='':
    basic_list1.append(name)
    name=input('Give me a name. <Enter with nothing else stops.')

print('\n')
    
basic_list2=[]
name=input('give me a name <Enter> with nothing else stops.')

while name!='':
    basic_list2.append(name)
    name=input('Give me a name. <Enter with nithing else stops.')
common_list=[]   
for word1 in basic_list1:
    for word2 in basic_list2:
        if word1==word2:
            if word1==word2:
                common_list.append(word1)
print(common_list)

