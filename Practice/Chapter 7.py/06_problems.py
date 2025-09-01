# 5! = 1 X 2 X 3 X 4 X 5 = 120
# 0! = 1
# 1! = 1
''' n! = n X (n-1) X (n-2) X (n-3) X .... X 1'''

# Write a program to find the factorial of a number using for loop

n = int(input(" Enter a number:"))
product = 1
for i in range(1, n+1):
    
    product = product * i  #(As, n means (n-1)th integer, So, n+1 means nth integer)
    # here this line iterates the value of i from 1 to n+1 and multiplies the value of i with the product

print(f"Factorial of {n} is {product}")


# Write a program to find the factorial of a number using while loop

n = int(input(" Enter a number:"))
product = 1
i = n

while (i >=1):
    product *= i # product = product * i
    i -= 1 # i = i - 1, decrement i by 1 after each iteration till i >= 1
print(f"Factorial of {n} is {product}")  # f-string is used to insert the value of n and product in the string.