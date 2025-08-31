#Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print(a1, "is the greatest number.")

elif(a2>a1 and a2>a3 and a2>a4):
    print(a2, "is the greatest number.")

elif(a3>a1 and a3>a2 and a3>a4):
    print(a3, "is the greatest number.")

else:
    print(a4, "is the greatest number.")
