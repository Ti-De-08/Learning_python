f = open("file_io.txt", "r") # r is the default 'mode', so it can be omitted
chant = f.read()
print(chant)
f.close()