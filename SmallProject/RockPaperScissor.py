import random

while True:
    choices = ["rock","paper","scissors"]

    bots = random.choice(choices)
    player = input("rock, paper, or scissors?: ").lower()

    print("player: ",player,"\nbots: ",bots)

#Player choose the same as bots
    if player == bots:
        print("Tie!")

#Player choose rock
    elif player == "rock" and bots == "paper":
        print("You lose!")

    elif player == "rock" and bots == "scissors":
        print("You win!")

#Player choose paper
    elif player == "paper" and bots == "scissors":
        print("You lose!")

    elif player == "paper" and bots == "rock":
        print("You win!")

#Player choose scissors
    elif player == "scissors" and bots == "rock":
        print("You lose!")

    elif player == "scissors" and bots == "paper":
        print("You win!")

#Player choose outside of choice
    elif player != choices:
        print("You can't pick that!")

    play_again = input("Play Again? (Y/n):").lower()

    if play_again != "y":
        break
