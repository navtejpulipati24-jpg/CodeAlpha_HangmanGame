"""
Hangman Game - CodeAlpha Python Programming Task 1
Goal: A simple text-based Hangman game where the player guesses
a word one letter at a time.
"""

import random

# A small predefined list of words (no file or API needed)
WORD_LIST = ["python", "hangman", "computer", "keyboard", "internship"]

MAX_WRONG_GUESSES = 6


def choose_word(word_list):
    """Randomly pick one word from the list."""
    return random.choice(word_list)


def display_progress(word, guessed_letters):
    """Show the word with unguessed letters as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORD_LIST)
    guessed_letters = []      # letters the player has already tried
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {MAX_WRONG_GUESSES} wrong guesses allowed.")
    print("=" * 40)

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: {word}")
            print("=" * 40)
            return

    # Loop ended because wrong_guesses reached the limit
    print("\n" + "=" * 40)
    print("Game Over! You ran out of guesses.")
    print(f"The word was: {word}")
    print("=" * 40)


def main():
    play_again = "yes"
    while play_again == "yes":
        play_hangman()
        play_again = input("\nPlay again? (yes/no): ").lower().strip()

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()