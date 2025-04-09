"""
    Name: hangman.py
    Author: Andrew Peterson
    Date: 04/09/2025
    Purpose: play a game of hangman
"""
import random

lives = 5


#generate a random word
with open("words.txt", "r") as file:
    lines = file.readlines()

random_word = random.choice(lines).strip()

#generate display
display = list("_" * len(random_word))

while lives > 0:
    letterFound = False
    print(display)
    guess = input("Enter a single letter guess: ")
    if len(guess) == 1:
        pass
    else:
        print("Please enter only one letter.")
        continue
    for i in range(len(random_word)):
        if guess == random_word[i]:
            display[i] = guess
            letterFound = True
    if letterFound == False:
        lives -= 1
        print(f"No such luck, lose a life. you have {lives} left.")
    if "_" not in display:
        break

if lives < 1:
    print(f"Your out of lives. you lose (the word was '{random_word}' by the way)")
else:
    print(f"Congratulations you win the word was '{random_word}'")