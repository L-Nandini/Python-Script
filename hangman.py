import random

def hangman_game():
    # List of words to guess
    words = ["python", "hangman", "programming", "developer", "algorithm", "function", "variable"]
    word_to_guess = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word_to_guess)  # Display blanks for the word
    attempts_left = 6  # Number of incorrect guesses allowed
    guessed_letters = set()  # Keep track of guessed letters

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word. Good luck!\n")

    while attempts_left > 0 and "_" in guessed_word:
        print("Word to guess: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")
        
        # Get input from the player
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.\n")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.\n")
            attempts_left -= 1

    # End of game messages
    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word: " + word_to_guess)
    else:
        print(f"Game over! The word was: {word_to_guess}")

# Run the game
hangman_game()
