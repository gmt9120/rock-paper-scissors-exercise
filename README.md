# Rock-Paper-Scissors Instructions

This is a game that lets you play riveting games of Rock-Paper-Scissors against a computer! Here is what you need to know and setup to run the game:

## Background
Ellie created this game to show she can apply python coding basics, set up repositories with proper files, and use version control best-practices in development.

The player's goal is to have fun! The player will first enter their name, then choose between 3 options: rock, paper, or scissors. The computer will also choose an option at random. If both the player and computer choose the same option, it's a tie game. Otherwise, scissors beats paper, paper beats rock, and rock beats scissors. 



## Setup

Step 1: Create a new repository. Clone this repository from GitHub, click "Open with GitHub Desktop," and save it to your local computer.

Step 2: Create an Anaconda virtual environment:

```sh
conda create -n rps-env python=3.8
```

Step 3: Activate the virtual environment:

```sh
conda activate rps-env
```

Step 4: Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```
*Note, no pip install is needed to play this game.

## Usage

To play the rock paper scissors game, run the python script from the command line:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```



## Future Development Plans

More enhancements are planned for this game, including adding a loop back to the Player choice step of the game so the user doesn't have to replay the program each time. 


## Enjoy!