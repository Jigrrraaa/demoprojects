import random

playing = True
counter = 0

# run untill user type 'n'
while playing:
    # use try catch to get int value if user pass something else return error
    try:
        # take input from from user
        num_dice = int(
            input("How many dice do you want to roll? (Enter 0 to quit): "))
        if num_dice == 0:
            print('Thanks for playing!')
            print(f'user has rolled dice {counter} times')
            break
        if num_dice < 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid number. Please enter an integer.")
        continue
    # ask user that do you want roll the dice.
    # use lower function to to consider caps later as well as part of input
    choice = input("Roll the dice? (y/n) :").lower()
    if choice == 'y':
        # empty list
        dice = []
        for i in range(num_dice):
            roll = random.randint(1, 6)
            # add each dire value in to list
            dice.append(roll)
            counter += 1
        print(f'{tuple(dice)}')
        print(f'user has rolled {counter} times')
    # stop the while loop if user does not want
    elif choice == 'n':
        print('Thanks for playing!')
        print(f'user has rolled dice {counter} times')
        break
    else:
        print('Invalid choice!')
