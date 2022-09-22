# Hangman Game

from random import randint
import sys
import time

# Creating an empty list for the words
words = []

# Opening the text file and filling in the words list
with open("words.txt", "r") as wordfile:
    for line in wordfile:
        words.append(line.strip())

# Assigning the number of lives
lives = 12
# Generating a random word for the user to guess
wordToGuess = words[randint(0, len(words))]
# Counts the number of guesses it takes to get the word
numGuesses = 0

# Creating how the word is shown e.g (a _ _ l _)
display = []
for letter in wordToGuess:
    display.append("_")


lettersGuessed = []
def userGuess():

    global guess
    global numGuesses

    while True:
        try:# Getting the users guess
            guess = input("Enter a letter you would like to guess: ").lower()
        except ValueError:
            # Msg printed when an invalid input occurs
            print("Please enter a valid letter")
            continue

        if len(guess) > 1:
            # Msg displayed when more then 1 letter is entered
            print("Please only enter 1 letter at a time")
            continue

        # Makes sure the input is a letter
        elif not guess.isalpha():
            print("Please enter a letter")
            continue

        # Makes it so you can't guess the same letter twice
        elif guess in lettersGuessed:
            print("You have already guessed this letter. Try another instead.")
            continue

        # Exits the loop once a valid input is entered
        else:
            break
    
    lettersGuessed.append(guess)
    numGuesses += 1

def letterCheck():

    global lives

    # Checks if the letter the user guesses is in the word
    if guess in wordToGuess:
        print("Good guess. The letter", guess, "is in the word")
        letters()
    else:
        # Removes a life if the letter isnt in the word
        lives -= 1
        printImage()
        # Checks if there are 0 lives left. If there is, ends the game
        if lives == 0:
            gameOver()
        print("Unlucky. Guess again")
        print("Current lives:", lives)

def letters():
    x = 0
    for letter in wordToGuess:
        if letter == guess:
            display[x] = guess
        x += 1

# Importing all the images and saving them in variables
with open("images/1wrong.txt", "r") as one:
    image1 = one.read()
    
with open("images/2wrong.txt", "r") as two:
    image2 = two.read()

with open("images/3wrong.txt", "r") as three:
    image3 = three.read()

with open("images/4wrong.txt", "r") as four:
    image4 = four.read()

with open("images/5wrong.txt", "r") as five:
    image5 = five.read()

with open("images/6wrong.txt", "r") as six:
    image6 = six.read()

with open("images/7wrong.txt", "r") as seven:
    image7 = seven.read()

with open("images/8wrong.txt", "r") as eight:
    image8 = eight.read()

with open("images/9wrong.txt", "r") as nine:
    image9 = nine.read()

with open("images/10wrong.txt", "r") as ten:
    image10 = ten.read()

with open("images/11wrong.txt", "r") as eleven:
    image11 = eleven.read()

with open("images/12wrong.txt", "r") as twelve:
    image12 = twelve.read()

# Prints the correct image based on number of incorrect guesses
def printImage():
    if lives == 11:
        print(image1)
    if lives == 10:
        print(image2)
    if lives == 9:
        print(image3)
    if lives == 8:
        print(image4)
    if lives == 7:
        print(image5)
    if lives == 6:
        print(image6)
    if lives == 5:
        print(image7)
    if lives == 4:
        print(image8)
    if lives == 3:
        print(image9)
    if lives == 2:
        print(image10)
    if lives == 1:
        print(image11)
    if lives == 0:
        print(image12)

# Displays a message and ends the game 
def gameOver():
    print("\n----------------------------------")
    print("Unlucky! Better luck next time.")
    print("----------------------------------\n")

    print("The word was:", wordToGuess)

    time.sleep(5)
    input("Enter any key to exit...")
    sys.exit()

# Starts the game
def play():
    print("Hangman\n~~~~~~~~~~~~~")
    print("Have fun playing!\n")

    # Initially prints the blank letter spaces
    print(display)
    # Loops while there are still letters to guess
    while "_" in display:
        userGuess()
        letterCheck()
        letters()
        print("Letters you have guessed",lettersGuessed)
        print(display)


play()
# Prints if the user correctly guesses the whole word
print("\n----------------------------------")
print("Well done! You guessed the whole word.")
print("It took you", numGuesses, "guesses to get the word")
print("----------------------------------\n")

print("Thanks for playing")
print("----------------------------------")

time.sleep(5)
input("Enter any key to exit...")