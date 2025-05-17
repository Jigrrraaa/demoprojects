import random

# declare choice as a list and create dict for emoji to assign each key
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '🪨', PAPER: '📄', SCISSORS: '✂️'}
choices = tuple(emojis.keys())

# function to return user choice


def get_user_choice():
    # take use choice as r, p,and s if any thing else print the error run the loop again
    while True:
        user_choice = input('Rock, Paper or Scissors? (r/p/s) :').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

# function to display the choices


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


# function to determine the winner of game


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')

# function for game which calls above function and run the game


def play_game():
    # run in loop until user quit
    while True:
        # get user choice
        user_choice = get_user_choice()

        # use random library to choose value from list of choice
        computer_choice = random.choice(choices)

        # print what user and computer has selected
        display_choices(user_choice=user_choice,
                        computer_choice=computer_choice)

        # check who win?
        determine_winner(user_choice=user_choice,
                         computer_choice=computer_choice)

        # ask user if user want to play game or not?
        should_continue = input('Continue? (y/n ?)').lower()
        if should_continue == 'n':
            break


# call the function
play_game()
