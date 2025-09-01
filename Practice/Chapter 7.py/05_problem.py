#Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter a number: "))
i = 1
sum = 0
while (i<=n):
    sum += i   # sum = sum + i
    i += 1     # i = i + 1, increment i by 1 after each iteration till i <= n
print(f"Sum of first {n} natural numbers is {sum}") 
# f-string is used to insert the value of n and sum in the string.