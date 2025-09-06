try:
    a = int(input("Hey, please enter a number: "))
    print(a)

except ValueError as v: #here ValueError is a built-in exception for invalid literal for int()
    
    print("ValueError occurred:", v)

except Exception as e: #here Exception is a base class for all built-in exceptions
    print("An error occurred:", e)


print("No error occurred, the number is:", a)

"""else is executed only when try block is executed successfully without any exception."""