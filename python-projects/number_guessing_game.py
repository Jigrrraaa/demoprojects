import os

#ask user 1 for choice number
try:
    choice = int(input('enter the choice number between 1 to 100 ?'))
except ValueError:
    print("Invalid number. Please enter an integer.")

#clean terminal after selecting choice number
os.system('cls')

#run in loop until user guess the choice number
isGuessed = False
while not isGuessed:
    guess = int(input('Guess the number between 1 to 100 ?'))
    if guess == choice:
        print("Congratulations! You guessed the number")
        isGuessed = True
        break
    elif 3 >= abs(guess - choice) <= 3 and guess != choice:
        print("You are almost there")
    elif guess > choice:
        print("Too High")
    elif guess < choice:
        print("Too low")
    else:
        print("invalid choice")
