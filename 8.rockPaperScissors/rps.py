# 2-Player Rock, Paper, Scissors Game

options = ["rock", "r", "paper", "p", "scissors", "s"]
player1wins = 0
player2wins = 0
gamesplayed = 0

# Gets the number of games the users want to play
def games():
    global numGames
    # Defines the choices the user can choose from
    choices = [1,3,5]
    while True:
        try:
            # Gets the user to input the number of games they want to play
            numGames = int(input("How many games would you like to play? (1, 3 or 5) "))
        # Message displayed when an invalid input is entered
        except ValueError:
            print("Please enter a valid number")
            continue
        # Message displayed when they enter an option not in the list
        if numGames not in choices:
            print("Please choose either 1, 3 or 5")
            continue
        # Exits the loop when a valid input is entered
        else:
            break

# Player 1's turn
def player1():
    global move1

    while True:
        try:
            # Gets the user to enter a move
            move1 = input("Player 1 - Select Rock, Paper or Scissors: ")
        except:
            # Message printed when an invalid input is entered
            print("Please enter a valid option")
            continue
        # Makes sure the user has entered a valid move
        if move1.lower() in options:
            break
        else:
            # Message printed when the option entered isn't in options
            print("Please choose Rock, paper or scissors")
            continue

# Player 2's turn
def player2():
    global move2

    while True:
        try:
            move2 = input("Player 2 - Select Rock, Paper or Scissors: ")
        except:
            print("Please enter a valid option")
            continue
        if move2.lower() in options:
            break
        else:
            print("Please choose Rock, paper or scissors")
            continue

# Working out who wins
def win():
    global move1
    # Setting player 1's move
    if move1.lower() == "r" or move1.lower() == "rock":
        move1 = "rock"
    elif move1.lower() == "p" or move1.lower() == "paper":
        move1 = "paper"
    elif move1.lower() == "s" or move1.lower() == "scissors":
        move1 = "scissors"
    global move2
    # Setting player 2's move
    if move2.lower() == "r" or move2.lower() == "rock":
        move2 = "rock"
    elif move2.lower() == "p" or move2.lower() == "paper":
        move2 = "paper"
    elif move2.lower() == "s" or move2.lower() == "scissors":
        move2 = "scissors"

    global player1wins
    global player2wins
    # Deciding who wins by comparing moves
    if move1 == "rock":
        if move2 == "rock":
            print("It's a tie! Play again.")
            # replays game if its a tie
            play()
        
        elif move2 == "paper":
            print("Player 2 wins!")
            # increments score count
            player2wins += 1

        elif move2 == "scissors":
            print("Player 1 wins!")
            player1wins += 1

    elif move1 == "paper":
        if move2 == "rock":
            print("Player 1 wins!")
            player1wins += 1
        
        elif move2 == "paper":
            print("Its a tie! Play again.")
            play()

        elif move2 == "scissors":
            print("Player 2 wins!")
            player2wins += 1
    
    elif move1 == "scissors":
        if move2 == "rock":
            print("Player 2 wins!")
            player2wins += 1

        elif move2 == "paper":
            print("Player 1 wins!")
            player1wins += 1
        
        elif move2 == "scissors":
            print("It's a tie! Play again.")
            play()



def start():
    print("Lets play Rock, Paper, Scissors!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    games()
    play()

def play():
    global gamesplayed
    
    # Loops until the correct number of games have been played
    while gamesplayed < numGames:
        player1()
        player2()
        win()
        # Displays the current score and number of games played
        print("-------------------------")
        print("The current score is: ")
        print("Player 1:", player1wins)
        print("Player 2:", player2wins)
        print("Games played:", gamesplayed+1)
        print("-------------------------")

        # Checks if the players wins are more then half of the total games
        # If so, then they have won so exits the loop
        if player1wins > numGames/2:
            break
        elif player2wins > numGames/2:
            break
        
        # increments the gamesplayed count
        gamesplayed += 1
    
    # Displays who wins the game
    if player1wins > player2wins:
        print("Player 1 wins! You're the best!")
    elif player2wins > player1wins:
        print("Player 2 wins! You're the best!")
    else:
        # Just in case, this should never happen
        print("Wow! It's a tie! You're just as good as each other")

# Runs the program
start()
    
