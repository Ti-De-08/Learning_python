Identity = ["Apple", "Banana", "Cherry", "14", "5.5", 360.60]
print(Identity[2])

Identity[2] = "Orange"
print(Identity[2])
print(Identity)

# Outputs suggests that the list is mutable
# The list can be changed, and the values can be updated

print(Identity[0:4])

'''List Methods'''
Identity.append("Milk")	#Adds an element at the end of the list


Identity.insert(1, "Orange")	#Adds an element at the specified position


Identity.remove("Apple")    #Removes the first item with the specified value

print(Identity.pop(4))	#Removes the element at the specified position

print(Identity)