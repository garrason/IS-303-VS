import random


def choose_word():
    # These words have five letters with no repeated letters.
    words = ["plant", "brick", "ghost", "flame", "sword"]
    return random.choice(words)


def get_guess(previous_guesses):
    # Keep asking until the player enters a valid, unused guess.
    while True:
        guess = input("Enter a five-letter word: ").strip().lower()

        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly five letters.")
        elif guess in previous_guesses:
            print("You already guessed that word. Try another.")
        else:
            return guess


def evaluate_guess(answer, guess):
    feedback = ""

    for i in range(len(answer)):
        if guess[i] == answer[i]:
            feedback += "G"
        elif guess[i] in answer:
            feedback += "Y"
        else:
            feedback += "-"

    return feedback


def display_guess(guess, feedback):
    print("Guess:   ", " ".join(guess.upper()))
    print("Feedback:", " ".join(feedback))
    print()


def has_won(answer, guess):
    return guess == answer