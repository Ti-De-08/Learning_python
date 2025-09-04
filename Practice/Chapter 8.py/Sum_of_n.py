#Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
.
.
.
sum(n) = 1 + 2 + 3 + 4 + 5.... (n-1) + n
=> sum(n) = sum(n-1) + n

'''

def sum(n):
    if(n == 1): # base condition to stop the recursion from going into infinite loop
        return 1
    
    return sum(n-1) + n

n = int(input("Enter an number: "))
print (sum(n))