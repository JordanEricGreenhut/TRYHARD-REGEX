myString = input('Please enter a string')

if (myString.isalpha() or ' '):

    def upperCaseFunction():
        upperCaseFunction()

    def myDecorator(func):
        print(myString.upper())

    upperCaseFunction = myDecorator(upperCaseFunction)

else: raise Exception("You entered a value that is not in the alphabet")