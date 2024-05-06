import random


def get_player_choice():
    choices = ('rock', 'paper', 'scissors')
    player_choice = input("Enter your choice ").lower()
    while player_choice not in choices:
        player_choice = input("Wrong choice.Enter choices again ").lower()
    return player_choice


def get_computer_choices():
    choices = ('rock', 'paper', 'scissors')
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Its a tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You Win"
    else:
        return "computer win"


def play_game():
    print("Welcome to Game ")
    player_choices = get_player_choice()
    print("player choice is " + player_choices)
    computer_choices = get_computer_choices()
    print("Computer choice is " + computer_choices)
    result = determine_winner(player_choices, computer_choices)
    print(result)


play_game()
