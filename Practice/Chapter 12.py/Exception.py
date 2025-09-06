try:
    a = int(input("Hey, please enter a number: "))
    print(a)

except Exception as e: #here Exception is a base class for all built-in exceptions
    print("An error occurred:", e)

print("This is the end of the program.")

"""The program will not crash even if an exception occurs.
 If the user enters a non-integer value, the program will catch the exception and print an error message.
 The try block will attempt to execute the code inside it. If an exception occurs,
 the exept block will handle the exception and print the error message."""