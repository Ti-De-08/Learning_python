"""Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’."""

with open('poem.txt') as file:
    poem = file.read()
    if ("Twinkle" in poem):
        print("Yes, the word contains in the poem.")
    else:
        print("No, the word is not present in the poem.")