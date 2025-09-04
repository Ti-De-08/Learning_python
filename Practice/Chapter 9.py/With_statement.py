file = open("file_io.txt", "r") # r is the default 'mode', so it can be omitted
chant = file.read()
print(chant)
file.close()

# the same code can be written using the "with" statement
# the "with" statement automatically closes the file after reading it

with open( "file_io.txt") as file:
    chant = file.read() #chant is a variable that stores the string returned by f.read() 
    print(chant)

# NOW YOU do not need to close the file explicitly

"""The "with" statement is used to wrap the execution of a block of code.
It is used to open a file and automatically close it after reading it."""