#Write a program to print the content of a list using while loops.

list = [ 1, 'two', 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']

index = 0
while(index < len(list)):
    print(list[index])     # prints the i-th element of the list
    index += 1            # increment i by 1 after each iteration

# The code above prints all the elements of the list.