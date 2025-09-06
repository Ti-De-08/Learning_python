l = [1, 2, 3, 4]

i = 0 # here i is used to keep track of the index of the item in the list

for item in l:
    print(f"The item number at index {i} is {item}")
    i+= 1

print("\nUsing enumerate() function:" )

for i, item in enumerate(l): #for i=index, item in enumerate of l
    print(f"The item number at index {i} is {item}")

# here i is the index of the item in the list and item is the value of the item at that index