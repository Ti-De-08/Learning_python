myList = [1, 2, 3, 4, 5]

squaredList = []

for item in myList:
    squaredList.append(item * item)
print (squaredList)

# List comprehension
print("\nList comprehension:")
squaredList = [item * item for item in myList]
print(squaredList)