#Attempt problem 1 using while loop

n = int(input("Enter a number: "))
i = 1 

while(i<=10):
    print(f"{n} X {i} = {n * i}") # this line is applicable for executing all number tables.
    i += 1 

    #f string is used to insert the value of n and i in the string.