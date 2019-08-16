def file_reader(file_name):

    file_to_be_read=open(file_name,'r')
    file_contents=file_to_be_read.readlines()
    file_to_be_read.close()
    return file_contents

def file_fixer(file_contents):
    words_in_file=set()
    for line in file_contents:
        temp=line.rstrip()
        temp_line=temp.split(' ')
        temp_set=set(temp_line)
        words_in_file=set.union(words_in_file,temp_set)
    return words_in_file

files_to_be_read=['trash.dat']
list_of_set_of_words_files=[]

for file_to_convert in files_to_be_read:
    
    print(file_fixer(file_reader(file_to_convert))
