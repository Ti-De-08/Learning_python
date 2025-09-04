
'''Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.'''

def generateTable(n): # here n is the number for which we want to generate the table
    table = "" # Create an empty string to store the table
    for i in range(1, 11): # Loop from 1 to 10 to generate the table
        table += f"{n} x {i} = {n*i}\n" # Append each line to the table string.
#the formula explains that we are using f-string formatting to create a string that contains the multiplication table.

    with open(f"tables/table_{n}.txt", "w") as f: # Open a file in write mode to save the table
        f.write(table) # Write the table string to the file.




for i in range(2, 21):
    generateTable(i)