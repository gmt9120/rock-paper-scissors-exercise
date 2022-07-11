# this is the "game.py" file...

from multiprocessing import RLock
from secrets import choice

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

### PROCESSING AND VALIDATING USER INPUTS ###

user_choice = input("Please choose either 'rock', 'paper', or 'scissors' and input it here:").lower()
print("You chose:", user_choice)
if user_choice not in ["rock", "paper", "scissors"]:
    print("Error. Please enter 'rock', 'paper', or 'scissors'")
    exit()

### SIMULATING COMPUTER SELECTION ###

computer_choice = choice(["rock", "paper", "scissors"])
print("The computer chose:", computer_choice)

### DETERMINING THE WINNER ###
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Rock beats scissors. You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Paper beats rock. You lose :(")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Scissors beats paper. You lose :(")
elif user_choice == "paper" and computer_choice == "rock":
    print("Paper beats rock. You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Scissors beats paper. You win!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Rock beats scissors. You lose :(")

print("Thanks for playing. Please play again!")