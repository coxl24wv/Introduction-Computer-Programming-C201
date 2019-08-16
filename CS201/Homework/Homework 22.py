#Homework 22
#Programmer Lauren Cox

one_dict={'a':'* ','b':'* ','c':'**','d':'**','e':'* ','f':'**','g':'**', \
          'h':'* ','i':' *','j':' *','k':'* ','l':'* ','m':'**','n':'**', \
          'o':'* ','p':'**','q':'**','r':'* ','s':' *','t':' *','u':'* ', \
          'v':'* ','w':' *','x':'**','y':'**','z':'* '}

two_dict={'a':'  ','b':'* ','c':'  ','d':' *','e':' *','f':'* ','g':'**', \
          'h':'**','i':'* ','j':'**','k':'  ','l':'* ','m':'  ','n':' *', \
          'o':' *','p':'* ','q':'**','r':'**','s':'* ','t':'**','u':'  ', \
          'v':'* ','w':'**','x':'  ','y':' *','z':' *'}

three_dict={'a':'  ','b':'  ','c':'  ','d':'  ','e':'  ','f':'  ','g':'  ', \
            'h':'  ','i':'  ','j':'  ','k':'* ','l':'* ','m':'* ','n':'* ', \
            'o':'* ','p':'* ','q':'* ','r':'* ','s':'* ','t':'* ','u':'**', \
            'v':'**','w':' *','x':'**','y':'**','z':'**'}

person_lowercase=input('Type in a lower case letter:')

for letter in person_lowercase:
    print(one_dict[letter],end='')
print()

for letter in person_lowercase:
    print(two_dict[letter],end='')
print()

for letter in person_lowercase:
    print(three_dict[letter],end='')
print()
