# Homework 18
# Programmer Lauren Cox
# Date of last revision 11-02-2016

lower_dict={'a':'*\n\n','b':'*\n*','c':'**\n' \
            ,'d':'**\n *','e':'*\n *','f':'**\n*' \
            ,'g':'**\n**','h':'*\n**','i':' *\n*' \
            ,'j':' *\n**','k':'*\n*','l':'*\n*\n*' \
            ,'m':'**\n*','n':'**\n *\n*','o':'*\n *\n*' \
            ,'p':'**\n*\n*','q':'**\n**\n*','r':'*\n**\n*' \
            ,'s':' *\n*\n*','t':' *\n**\n*','u':'*\n\n**' \
            ,'v':'*\n*\n**','w':' *\n**\n *','x':'**\n\n**'\
            ,'y':'**\n *\n**','z':'*\n *\n**'}

person_lowercase=input('Type in a lower case letter:')

if person_lowercase in lower_dict:
    print(lower_dict[person_lowercase])
    
#ne
