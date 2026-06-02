#!/usr/bin/env python3
"""
CodeAlpha Python Internship
Task 1: Hangman Game

A classic console-based Hangman Game where players guess letters to reveal 
a hidden word. Includes progress visualization and user-friendly interface.
"""

import random

# Predefined list of words for the game
WORDS_POOL = [
    "PYTHON",
    "DEVELOPER",
    "INTERNSHIP",
    "PROGRAMMING",
    "CODEALPHA",
    "SOFTWARE",
    "ALGORITHM",
    "COMPUTING"
]

# Visual ASCII representation of hangman stages (0 to 6 incorrect guesses)
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Maximum allowed incorrect attempts corresponding to hangman stages
MAX_INCORRECT_ATTEMPTS = 6


def get_random_word(word_list):
    """
    Selects a random word from the provided word list and returns it in uppercase.
    """
    return random.choice(word_list).upper()


def display_game_status(secret_word, guessed_letters, incorrect_attempts):
    """
    Displays the current state of the game:
    - Hangman ASCII art
    - Secret word with guessed letters revealed and others masked as '_'
    - Guessed letters so far
    - Number of remaining incorrect attempts
    """
    # Print the Hangman stage
    print(HANGMAN_STAGES[incorrect_attempts])
    
    # Generate the masked/revealed secret word display
    word_display = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print(f"Word: {' '.join(word_display)}")
    
    # Display statistics
    remaining_attempts = MAX_INCORRECT_ATTEMPTS - incorrect_attempts
    print(f"Remaining Incorrect Attempts: {remaining_attempts}")
    
    # Sort and display guessed letters
    sorted_guesses = sorted(list(guessed_letters)) if guessed_letters else []
    print(f"Guessed Letters: {', '.join(sorted_guesses) if sorted_guesses else 'None'}")
    print("-" * 40)


def get_user_guess(guessed_letters):
    """
    Prompts the user to enter a single alphabetical character.
    Validates input to ensure it is:
    - Exactly 1 character long
    - Alphabetic
    - Not already guessed
    """
    while True:
        guess = input("Enter a letter to guess: ").strip().upper()
        
        # Validation checks
        if len(guess) != 1:
            print("Invalid input! Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Invalid input! Please enter an alphabetical letter (A-Z).")
        elif guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman_session():
    """
    Manages a single session of Hangman from start to finish.
    """
    secret_word = get_random_word(WORDS_POOL)
    guessed_letters = set()
    incorrect_attempts = 0
    
    print("\n" + "=" * 40)
    print("        WELCOME TO HANGMAN GAME!        ")
    print("=" * 40)
    print("Try to guess the secret word letter by letter.")
    
    # Set of unique letters in the secret word that must be guessed
    secret_word_letters = set(secret_word)
    
    while incorrect_attempts < MAX_INCORRECT_ATTEMPTS:
        display_game_status(secret_word, guessed_letters, incorrect_attempts)
        
        # Get a validated guess from the user
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)
        
        # Process the guess
        if guess in secret_word_letters:
            print(f"\nGood job! '{guess}' is in the secret word!")
            # Check if all letters have been guessed
            if secret_word_letters.issubset(guessed_letters):
                display_game_status(secret_word, guessed_letters, incorrect_attempts)
                print("*** CONGRATULATIONS! You guessed the word! ***")
                print(f"The word was indeed: {secret_word}\n")
                return
        else:
            print(f"\nOops! '{guess}' is NOT in the secret word.")
            incorrect_attempts += 1
            
    # Out of attempts - Game Over
    display_game_status(secret_word, guessed_letters, incorrect_attempts)
    print("=== GAME OVER! You ran out of attempts. ===")
    print(f"The secret word was: {secret_word}\n")


def main():
    """
    Main controller for the game. Allows players to play multiple rounds.
    """
    while True:
        play_hangman_session()
        
        # Ask user if they want to play again
        replay = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\nThank you for playing Hangman! See you next time!")
            break


if __name__ == "__main__":
    main()
