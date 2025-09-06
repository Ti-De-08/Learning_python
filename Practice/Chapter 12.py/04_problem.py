
try:
    a = int(input("Enter a Number: "))
    b = int(input("Enter another Number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite:", z)
