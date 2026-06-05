#   TASK 1: Hangman Game
#   Concepts: random, while loop, if-else, strings, lists

import random

#   STEP 1: Word list (5 predefined words)

WORDS = ['python', 'hangman', 'computer', 'keyboard', 'program']

# Hangman stages — 7 stages (0 wrong = safe, 6 wrong = dead)
HANGMAN = [
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """
]

#   STEP 2: Display the current word with blanks

def display_word(secret_word, guessed_letters):
    """
    Shows the word with correctly guessed letters revealed.
    Unguessed letters are shown as underscore _.
    Example: if word is 'python' and user guessed 'p' and 'n'
             it shows: p _ _ _ _ n
    """
    result = ''
    for letter in secret_word:
        if letter in guessed_letters:
            result += letter + ' '   # Show the letter
        else:
            result += '_ '           # Hide the letter
    return result.strip()

#   STEP 3: Check if player has won

def is_won(secret_word, guessed_letters):
    """
    Returns True if every letter in the word has been guessed.
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

#   STEP 4: Main game function

def play_hangman():
    """
    Main function that runs the Hangman game loop.
    """

    print("=" * 45)
    print("       Welcome to HANGMAN GAME!")
    print("  Guess the word — you have 6 wrong chances.")
    print("=" * 45)

    # Pick a random word from the list
    secret_word = random.choice(WORDS)

    guessed_letters = []   # Letters the player has guessed
    wrong_guesses   = 0    # Count of incorrect guesses
    max_wrong       = 6    # Maximum allowed wrong guesses

    # Keep playing until win or lose
    while wrong_guesses < max_wrong:

        # Show hangman drawing
        print(HANGMAN[wrong_guesses])

        # Show current word state
        print(f"  Word:    {display_word(secret_word, guessed_letters)}")
        print(f"  Wrong:   {wrong_guesses}/{max_wrong}")
        print(f"  Guessed: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print()

        # Check if player has already won
        if is_won(secret_word, guessed_letters):
            print(f"  Congratulations! You guessed the word: '{secret_word}' 🎉")
            break

        # Take input from player
        guess = input("  Enter a letter: ").lower().strip()

        # Validate input — must be a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("  Please enter a single letter only!\n")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print(f"  You already guessed '{guess}'. Try a different letter!\n")
            continue

        # Add to guessed list
        guessed_letters.append(guess)

        # Check if guess is correct or wrong
        if guess in secret_word:
            print(f"  Good guess! '{guess}' is in the word. ✅\n")
        else:
            wrong_guesses += 1
            print(f"  Wrong! '{guess}' is not in the word. ❌\n")

    # If loop ended because wrong_guesses reached max
    else:
        print(HANGMAN[6])
        print(f"  Game Over! You ran out of chances.")
        print(f"  The word was: '{secret_word}' 💀")

    print()
    print("=" * 45)


#   STEP 5: Ask to play again

def main():
    """
    Runs the game and asks if player wants to play again.
    """
    while True:
        play_hangman()

        again = input("  Play again? (yes / no): ").lower().strip()
        if again not in ['yes', 'y']:
            print("\n  Thanks for playing Hangman! Bye! 👋")
            break
        print("\n  Starting a new game...\n")


# Run the program
if __name__ == "__main__":
    main()
