# Import a module.
import random


# Get and validate the player's choice.
def get_player_choice():
    while True:
        player_choice = input(
            "Enter your choice (rock, paper, scissors): "
        ).strip().lower()

        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please try again.")


# Determine the result from the player's perspective.
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"
    else:
        return "loss"


# Run the entire game.
def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    # Ask for a positive, odd number of rounds.
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if rounds <= 0:
            print("Please enter a number greater than zero.")
        elif rounds % 2 == 0:
            print("The number must be odd. Please try again.")
        else:
            break

    # Start counters at 0.
    player_wins = 0
    player_losses = 0
    computer_wins = 0
    computer_losses = 0
    completed_rounds = 0

    # Play until all counted rounds are finished.
    while completed_rounds < rounds:
        print()
        player_choice = get_player_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)

        # Handle the result and update the counters.
        if result == "tie":
            print("Tie! Play again.")
            continue
        elif result == "win":
            print("You won!")
            player_wins += 1
            computer_losses += 1
        else:
            print("You lost!")
            player_losses += 1
            computer_wins += 1

        completed_rounds += 1

    # Display the final results after the loop finishes.
    print()
    print("-------------------------------------------")
    print(f"Score — You: {player_wins} | Computer: {computer_wins}")
    print(f"Your record: {player_wins} wins, {player_losses} losses")
    print(f"Computer record: {computer_wins} wins, {computer_losses} losses")

    if player_wins > computer_wins:
        print("You win!!!")
    else:
        print("The computer wins!")

    print("Thanks for playing!")


# Start the program.
if __name__ == "__main__":
    play_game()