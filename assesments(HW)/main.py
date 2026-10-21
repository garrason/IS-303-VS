from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won
)


def main():
    print("Welcome to Mystery Wordle!")
    print("Guess the five-letter word.")
    print()
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word")

    play_again = "yes"

    while play_again == "yes" or play_again == "y":
        answer = choose_word()
        previous_guesses = []
        won = False

        # Valid guesses are stored in the list and count as attempts.
        while len(previous_guesses) < 6:
            print()
            print(f"Attempt {len(previous_guesses) + 1} of 6")

            guess = get_guess(previous_guesses)
            previous_guesses.append(guess)

            feedback = evaluate_guess(answer, guess)
            display_guess(guess, feedback)

            if has_won(answer, guess):
                print("Congratulations! You solved the puzzle.")
                won = True
                break

        if not won:
            print(f"Maybe next time. The answer is {answer.upper()}.")

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()