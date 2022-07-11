# this is the "game.py" file...

from multiprocessing import RLock
from secrets import choice

print("Rock, Paper, Scissors, Shoot!")

### PROCESSING AND VALIDATING USER INPUTS ###

user_choice = input("Please choose rock, paper, or scissors and input it here:").lower()
print("You chose", user_choice, "!")
if user_choice not in ["rock", "paper", "scissors"]:
    print("Error. Please enter rock, paper, or scissors")
    exit()

### SIMULATING COMPUTER SELECTION ###

computer_choice = choice(["rock", "paper", "scissors"])
print("The Computer chose", computer_choice, "!")