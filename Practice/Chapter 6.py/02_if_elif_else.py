
'''This is if_elif_else ladder. It is used to check multiple conditions.'''

a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("You can vote")
elif(a<0):
    print("Invalid age! Please enter a valid age.")
elif("a==0"):
    print("You are not born yet. Please wait for some time!")

else:
    print("You are below the age of consent. You cannot vote")

print("Thank you for using the program")

