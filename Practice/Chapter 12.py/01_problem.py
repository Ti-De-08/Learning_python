try:
    with open("1.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")     

# The code above reads the contents of a file named "1.txt" in read mode and prints it to the console.
try:
    with open("2.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")


try:
    with open("3.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")

print("End of the program.")

# 6//2 here // "double slash" means "integer division" in Python.
# The type of 6//2 is int.
# The type of 6/2 is float because it is a "single slash" division which returns a float. 