'''Write a python function to print first n lines of the following pattern:
***
** 
*
    for n = 3
'''



def pattern(n):
    if(n==0): #base condition to stop the recursion
        return #return nothing
    print("*" * n) # print the "*"  n times
    pattern(n-1) # call the function recursively with n-1. run the pattern function again with n-1.


pattern(5) #call the function with n = 3