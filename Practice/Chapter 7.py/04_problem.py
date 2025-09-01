#Write a program to find whether a given number is prime or not.

"""Prime number is a number that is greater than 1 and divided by 1 or itself only.
1 is not a prime number. The number 1 has only 1 factor.
 For a number to be classified as a prime number, it should have exactly two factors."""


n = int(input("Enter a number: "))

for i in range(2, n): # range(2, n) will generate numbers from 2 to n-1
    if (n%i) == 0:
        print(n, "is not a prime number")
        break
else:
    print(n, "is a prime number")



