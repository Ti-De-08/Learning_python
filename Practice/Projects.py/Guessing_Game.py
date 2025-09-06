"""
PROJECT 2 – THE PERFECT GUESS
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module."""

import random

n = random.randint(1, 100)  # Generate a random number between 1 and 100

print("Welcome to the guessing game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")
print("Good luck!")

a = -1 # Initialize a variable to store the user's guess
guesses = 1 #As it would take atleast one guess to get the number

while(a != n): # Loop until the user guesses the correct number

    # Prompt the user for a guess 
    a = int(input("Enter your guess:\n"))

    if(a > n): # If the guess is higher than the number
        # Print a hint to the user
        print("No, Guess a lower number please.")
        guesses += 1 # Increment the number of guesses

    elif(a < n):# and_If(elif) the guess is lower than the number
        # Print a hint to the user
        print("No, Guess a higher number please.")
        guesses += 1 # Increment the number of guesses
    
    # When the guess is correct, congratulate the user and display the number of guesses
    else:
        print(f"Congratulations! You have guessed the number {n} correctly!")
        print(f"It took you {guesses} guesses.")