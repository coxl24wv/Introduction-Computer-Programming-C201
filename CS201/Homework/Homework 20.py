# Homework 20
# Programmer Lauren Cox
# Date of last revision 1-03-2016
# Vigenere Cipher_decrypt

M=input('Type in a simple string of upper case letters no spaces:')
k=input('Type in a upper case key:')

for position in range(len(M)):
    print(chr((ord(M[position])-65+26-(ord(k[position%len(k)])-65))%26+65),end="")



