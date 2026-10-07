#import a module
import random

#get and validate a players choice 
def get_player_choice():

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

#determine results 
def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
        ):
        return "You win!"
    else:
        return "Computer wins!" 
    
#print the results of the game
def play_game():

    print("Welcome to Rock, Paper, Scissors!")
    player_choice = get_player_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)   

    