import os

# Specify the directory (change this to the path you want)
directory = "C:/"

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
# for item in contents:
print(contents)

'''Explanation:
os.listdir(directory) returns a list of all files and directories in the specified path.
"." represents the current directory.
The program prints each item in the directory.+'''