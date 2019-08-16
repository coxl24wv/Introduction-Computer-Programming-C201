# Homework 17
# Programmer Lauren Cox
# Date of last revision 18-02-2016



infile=open('Homeworkfile17.py','r')
infile_list=[]

file_contents=infile.readlines()
my_dict={}
infile.close()
for line in file_contents:
    clean_line=line.rstrip()  
    word=clean_line.split(',') 
    my_dict[word[0]]=word[1]

x=input('Type in one of the first words:')
if x in my_dict:
    print(my_dict[x])
    

 
