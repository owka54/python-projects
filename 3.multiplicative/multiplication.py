# Creating a multiplication table

# List of valid numbers the user can input
nums = [1,2,3,4,5,6,7,8,9,10,11,12]

# Gets the input from the user
while True:
    try:
        selection = int(input("What number do you want to see a multiplication table for? (1-12) "))
    # If something other then a number is entered, display this error message and continue the loop
    except ValueError:
        print("Please enter a valid number")
        continue
    # If number entered is not between 1 and 12, display this message and continue the loop
    if selection not in nums:
        print("Please chose a value between 1 and 12")
        continue
    # Break the loop if a valid input is given
    else:
        break


print("Multiplication table for:", selection)
print("--------------------------")
# loops through the nums list
for num in nums:
    # Prints a message in the form (1 x 2 = 2) 
    print(num, "x", selection, "=", selection * num)
print("--------------------------")