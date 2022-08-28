# Dice roll

from random import randint

def roll():
    # Generates a random number between 1 and 6 to simulate a dice roll
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)

    # Prints what the user rolled
    print("You rolled a", dice1, "and a", dice2)

# Gets the number of times the user would like to roll the dice
while True:
    try:
        times = int(input("How many times would you like to roll? "))
    # Makes sure the user enters a number
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        break

# Rolls the dice the amount of times specified by the user
x = 1
while x <= times:
    roll()
    x += 1

