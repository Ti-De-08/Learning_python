""" Write a LIST COMPREHENSION to print a list which contains the multiplication table of a
user entered number."""


n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(f"The multiplication table of {n} is:")
print(table)