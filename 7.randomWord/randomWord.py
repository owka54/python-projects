# Picking a random word from a word list

from random import randint

# Creates an empty list
wordlist = []

# Opens the file with all the words
with open("words.txt", "r") as words:
    # Iterates through each line in the text file
    for line in words:
        # Appends the content of the line to the wordlist
        wordlist.append(line)

# Generates a random number to selct a word at random
randword = wordlist[randint(0, len(wordlist))]

# Prints message to show a word is being picked
print("Picking out a random word from the list...")
print("...")
print("...")
print("...")
print("Word found")
# Prints the word that was chosen at random
print("\nThe word that was chosen is:", randword)