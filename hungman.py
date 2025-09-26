import random

def hangman():
    # List of predefined words
    words = ["apple", "banana", "grapes", "orange", "cherry"]
    word = random.choice(words)  # Randomly choose a word
    guessed = "_" * len(word)    # Initially all blanks
    guessed = list(guessed)
    attempts = 6                 # Player gets 6 wrong guesses
    guessed_letters = []         # Track guessed letters

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts}")

        print(" ".join(guessed))

    # Win/Loss condition
    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()







