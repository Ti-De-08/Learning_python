"""Write a program to print the following star pattern.
  *
 ***
***** 
for n = 3"""

n = int(input("Enter  a number: "))

for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1)) # 2*i-1 is the formula for the number of stars in each row
# eplaination:
# n = 3
# i = 1
# " "*(3-1) + "*"x(2*1-1) = " "x(2) + "*"x(1) = "  " + "*" = "  *"
# repeat the process for i = 2 and i = 3

# Another way to solve the problem:
n = int(input("Enter  a number: "))

for i in range(1, n+1):
    print(" " * (n-i), end = "") # end = '' is used to avoid the new line as the print function automatically prints a new line
    print("*" * (2*i-1), end = '') #(2*i-1) is the formula for the odd number of stars in each row
    print("") # to print a new line after each row

# the formula above explains that:
# n = 3
# i = 1 
# " " * (3-1) = "  "
# "*" * (2*1-1) = "*" * 1 = "*"
# "  " + "*" = "  *"
# repeat the process for i = 2 and i = 3