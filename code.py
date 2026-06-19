import random
words = ["infosys", "apple", "cognizant", "oracle", "microsoft"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")
print("Hint: Name of Famous Companies !!!")
while incorrect_guesses < max_incorrect:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only one alphabet letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Correct guess!\n")
    else:
        incorrect_guesses += 1
        remaining = max_incorrect - incorrect_guesses
        print(" Wrong guess! ")
        print("Remaining incorrect guesses:", remaining, "\n")

if incorrect_guesses == max_incorrect:
    print(" Game Over!")
    print("The correct word was:", secret_word)

