f = open("file_io.txt", "rb")
chant = f.read()
print(chant)
f.close()

''' "open" is a built-in function that opens a file and returns a file object'''
''' f.read() reads the contents of the file and returns it as a string. '''
# chant is a variable that stores the string returned by f.read()
''' f.close() closes the file object f. It is a duty to close the file after reading it.'''
# If the file is not closed, it will remain open and consume system resources.
''' there are two ways to open a file: read mode and write mode'''
# read mode is the default mode, so it can be omitted
# read mode is used to read the contents of a file
# write mode is used to write data to a file
# write mode will overwrite the contents of the file
# if the file does not exist, it will be created
# if the file exists, it will be truncated(emptied) before writing. 