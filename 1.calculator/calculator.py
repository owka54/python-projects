# Basic calculator program

# Function for user to input the first number
def num1():

    global firstnum

    # Loops until a valid number is entered
    while True:
        try:
            num = int(input("Enter the first number: "))
            
        except ValueError:
            print("Please enter a valid number ")
            continue
        else:
            break
    
    firstnum = num

# Function to get the operation the user wants to do
def oprtr():

    global operation 

    # List of valid inputs for checking
    valid = ["+", "-", "*", "/"]

    while True:
        sign = input("Enter the operator you would like to use (+, -, *, /): ")
        if sign not in valid:
            print("Please enter a valid operator from the list")
            continue
        else:
            break

    operation = sign

def num2():

    global secondnum

    while True:
        try:
            num = int(input("Enter the second number: "))
            
        except ValueError:
            print("Please enter a valid number ")
            continue
        else:
            break

    secondnum = num

# Function to calculate the answer depending on the inputs
def calc(firstnum, secondnum, operation):

    global answer

    if operation == "+":
        answer = firstnum + secondnum
    elif operation == "-":
        answer = firstnum - secondnum
    elif operation == "*":
        answer = firstnum * secondnum
    elif operation == "/":
        answer = firstnum / secondnum

# Main function to run the program 
def calculator():
    
    # Calling functions to get user inputs
    num1()
    oprtr()
    num2()
    calc(firstnum, secondnum, operation)

    # Displays what the calculation is and then the answer
    print("Your calculation is:", firstnum, operation, secondnum)
    print("The answer is:", answer)

    # Loops until a valid input is entered, either runs the program
    # again or closes it depending on user input
    while True:
        run = input("Would you like to do another calculation? (Yes or no) ")
        if run.lower() == "yes":
            calculator()
            break
        elif run.lower() == "no":
            # Closing program message
            print("\n~~~~~~~~")
            print("Goodbye")
            print("~~~~~~~~")
            break
        else:
            continue

# Message displayed on program open
print("---------------------")
print("Opening Calculator...")
print("---------------------\n")

# Runs the program
calculator()
