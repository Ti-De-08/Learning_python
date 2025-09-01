#Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}") 
    # curly braces are used to insert the value of n and i in the string. 
    # it is called f-string. 
    # curly braces with a variable inside it are replaced by the value of the variable.