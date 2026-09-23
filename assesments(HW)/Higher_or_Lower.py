import random
play_again = "y"
while play_again == "y":

    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guess_count = 0
    guess = int(input("Enter your guess: "))

    # filter out invalid guesses and increment the guess count only for valid guesses
    while guess != secret_number:
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        else:
            guess_count += 1

            # The Game is here!
            if guess < secret_number:
                print("Higher!")
            elif guess > secret_number:
                print("Lower!")

        guess = int(input("Enter your guess: "))

    # Count the final correct guess
    guess_count += 1

    # print out a congratulations message when the user guesses the number correctly
    print("Congratulations! You guessed the number:", secret_number)

    # count the number of guesses and give a different message based on the number of guesses
    print("It took you", guess_count, "guesses.")

    if guess_count <= 3:
        print("Amazing!")
    elif guess_count <= 5:
        print("Impressive!")
    elif guess_count <= 7:
        print("Good job!")
    elif guess_count <= 9:
        print("Took a little longer, but you got there!")
    else:
        print("You need to lock in.")

    # Ask the user if they want to play again
    play_again = input("Would you like to play again? (Y/N): ").lower()
    #thank the player for playing the game when choosing to exit!
    if play_again == "n":
        print("Thanks for playing!")