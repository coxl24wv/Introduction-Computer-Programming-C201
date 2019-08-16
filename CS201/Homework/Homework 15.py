#Homework 15
#Programmer Lauren Cox
#Date of Last Revision 21-4-2016

foundPrimes = 2 
primes = [2,3]
currentNumber = 5

userInput = int(input("Give me a number:"))


primeIndex = 1

while foundPrimes < userInput:
    checkNumber = True
    if primes[primeIndex] * primes[primeIndex] < currentNumber + 1:
        primeIndex += 1
    for x in range(1,primeIndex):
        if currentNumber % primes [x] == 0:
            checkNumber = False
            break
    if checkNumber:
        primes.append(currentNumber)
        foundPrimes += 1
    currentNumber +=2

print(currentNumber)
