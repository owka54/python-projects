# Sort a list of words in alphabetical order

# Creates an empty list for words to be added to
words = []

# Prints a message explaining how to stop adding more words
print("To stop adding words to the list enter (STOP123)")
# Loops until the user wants to stop adding words
while True:
        # Gets the user to enter a word to be added to the list
        word = input("Enter a word to add to the list: ")
        # Stops the loop when the user enters the stop keyword
        if word == "STOP123":
            break
        # Adds the entered word to the list
        words.append(word)

# Prints the list of words the user entered
print("The list you made is: ")
print(words)
print("----------------")

# Prints the sorted list
print("The sorted list is: ")
sorted_words = sorted(words)
print(sorted_words)
print("----------------")