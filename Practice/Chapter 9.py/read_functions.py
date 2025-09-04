hk = open("file_io.txt", "r") # r is the default 'mode', so it can be omitted

'''lines = hk.readlines()

print(lines, type(lines))'''
#readlines function reads the contents of the file and returns it as a list of strings
#each string in the list represents a line in the file


'''line1 = hk.readline()
print(line1, type(line1))
line2 = hk.readline()
print(line2, type(line2))
line3 = hk.readline()
print(line3, type(line3))
line = hk.readline()
print(line, type(line))
line = hk.readline()
print(line == "", type(line))'''
#readline function reads the contents of the file line by line

line = hk.readlines()

while (line != ""):
    print(line)
    line = hk.readline()

hk.close()