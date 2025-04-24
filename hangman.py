"""
    Name: hangman.py
    Author: Andrew Peterson
    Date: 04/09/2025
    Purpose: play a game of hangman
"""
import random
import tkinter as tk

# Create the main window
game = tk.Tk()
game.title("Hangman")

lives = 5


#generate a random word
with open("words.txt", "r") as file:
    lines = file.readlines()

random_word = random.choice(lines).strip()

#generate display
display = list("_" * len(random_word))

display_label = tk.Label(game, text=" ".join(display), font=("Arial", 16))
display_label.pack(pady=10)
guess = tk.Entry(game, font=("Arial", 14), width=5)
guess.pack(pady=20)
response = tk.Label(game, text=f"Lives: {lives}", font=("Arial", 14))
response.pack(pady=30)
def input_guess():
    global lives
    letterFound = False
    user_guess = guess.get().strip().lower()
    guess.delete(0, tk.END)
    if len(user_guess) != 1 or not user_guess.isalpha():
        response.config(text="Please enter a single letter.")
        return
    for i in range(len(random_word)):
        if user_guess == random_word[i]:
            display[i] = user_guess
            letterFound = True
    if not letterFound:
        lives -= 1
        response.config(text=f"No such luck, lose a life. You have {lives} left.")

    display_label.config(text=" ".join(display))

    if "_" not in display:
        response.config(text=f"Congratulations! You win. The word was '{random_word}'.")
        guess.config(state="disabled")

    if lives <= 0:
        response.config(text=f"You're out of lives! The word was '{random_word}'.")
        guess.config(state="disabled")
button = tk.Button(game, text="Submit", command=input_guess)
button.pack(pady=5)

game.mainloop()