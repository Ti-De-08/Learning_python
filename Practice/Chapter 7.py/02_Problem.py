#Write a program to greet all the person names stored in a list ‘l’ and which startswith S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
        


l = input("What's your name: ")

#for l: # here name is a variable that stores the current element of the list
if(l.startswith('S')): # checks if the name starts with 'S'
        print(f"Hello, {l}!") # prints the name
else:
        print(f"Sorry, {l} your name does not start with 'S'")


# The code above greets all the names stored in the list 'l' that start with 'S'.

      