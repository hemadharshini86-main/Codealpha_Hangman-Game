
# Hangman Game in Python

import random

# Predefined list of words
words = ["infosys", "apple", "cognizant", "oracle", "microsoft"]

# Randomly choose a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")
print("Hint: Name of Famous Companies !!!")

# Game loop
while incorrect_guesses < max_incorrect:

    # Display the word with blanks
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check if player guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only one alphabet letter.\n")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correct or incorrect
    if guess in secret_word:
        print(" Correct guess!\n")
    else:
        incorrect_guesses += 1
        remaining = max_incorrect - incorrect_guesses
        print(" Wrong guess! ")
        print("Remaining incorrect guesses:", remaining, "\n")

# If player loses
if incorrect_guesses == max_incorrect:
    print(" Game Over! Better luck next time")
    print("The correct word was:", secret_word)

