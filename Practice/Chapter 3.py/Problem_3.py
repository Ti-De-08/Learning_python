#Write a program to detect double space and alphabets in a string.

string = "Don't practice until you get it right  Practice until you can't get it wrong  "
print(string.find("  ")) 
print(string.replace("  ", "! ")) # replace() method is used to replace a string with another string.

print(string) #strings are immutable in python. Runnig a function on a string does not change the original string.
