S = {1, 5, 32, 5, 1, 5, "Tirtha"}
print(S, type(S))

print(len(S)) #avoids duplicates

S.add(10)
print(S)

S.remove(32)
print(S) #S.remove(32) #throws error if element is not present
S.remove(32)
print(S) #S.remove(32) #throws error if element is not present

