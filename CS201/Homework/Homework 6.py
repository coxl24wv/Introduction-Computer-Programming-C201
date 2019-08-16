# sixth Program/Homework 6
# Programmer Lauren Cox

a=int(input('Type in a interger:'))

b=['one','two','three','four','five','six','seven','eight','nine', \
   'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
   'seventeen','eighteen','nineteen','twenty']

c=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']


thousand=a//1000
if thousand>0:
    print(b[thounsand-1],'thousands',end=' ')
a=a%1000

hundred=a//100
if hundred>0:
    print(b[hundred-1],'hundred',end=' ')
a=a%100


if 20<=a<100:
    tens=a//10
    if tens>0:
        print(c[tens-1],end=' ')
        a=a%10
        
        if 1<=a<10:
            one=a//1
            print(b[one-1],end=' ')

elif a<=19:
    print(b[a-1])

