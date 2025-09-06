a = int( input("Hey, please enter a number: "))
b = int( input("Hey, please enter another number: "))

if (b == 0):
    raise ZeroDivisionError("Sorry, you cannot divide by zero.") #here ZeroDivisionError is a built-in exception for division by zero

else:
    c = a/b
    print( "The result is: ", c)

#if the user enters 0 for b, a ZeroDivisionError will be raised with the error message and the program will crash.