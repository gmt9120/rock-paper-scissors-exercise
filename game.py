# this is the "game.py" file...

from multiprocessing import RLock
from secrets import choice


print("Rock, Paper, Scissors, Shoot!")
user_input = input("Please choose rock, paper, or scissors and input it here:")
print(user_input)
def user_choice():
    "Rock"
    "Paper"
    "Scissors"
if user_input == "Rock":
    user_choice == "Rock"
elif user_input == "rock":
    user_choice == "Rock"
elif user_input == "ROCK":
    user_choice == "Rock"
elif user_input == "Paper":
    user_choice == "Paper"
elif user_input == "paper":
    user_choice == "Paper"
elif user_input == "PAPER":
    user_choice == "Paper"
elif user_input == "Scissors":
    user_choice == "Scissors"
elif user_input == "scissors":
    user_choice == "Scissors"
elif user_input == "SCISSORS":
    user_choice == "Scissors"
else:
    quit()