#Homework 21
#Programmer Lauren Cox
#Date of Last Revision 25-4-2016

file_contents = []

while 1:
    print("1. Read a file called Homeworkfile21.py")
    print("2. Save a file called Homeworkfile21.py")
    print("3. Add a record to Homeworkfile21.py")
    print("4. Delete a record from Homeworkfile21.py")
    print("5. Change record in Homeworkfile21.py")
    print("6. Sort list in file Homeworkfile21.py")
    print("7. Do nothing and end program")

    userchoice = int(input("Choose a number:"))
    
    if userchoice == 1:
        infile = open("Homeworkfile21.py")
        file_contents = infile.readlines()
        for i in range (len(file_contents)):
            file_contents[i] = file_contents[i].replace ("\n","")
        infile.close()
        print(file_contents)
    elif userchoice == 2:
        outfile = open("Homeworkfile21.py","w")
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

