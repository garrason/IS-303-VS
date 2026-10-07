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