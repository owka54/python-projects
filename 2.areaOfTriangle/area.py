# Calculate the area of a triangle

# Gets the user to input a height, loops until a valid number is given
go = True
while go:
    try:
        height = float(input("Enter the height of the triangle: "))
    
    except ValueError:
        # Error message if invalid input is given
        print("Please enter a valid number")
        continue
    # Breaks the loop if the value given is valid
    else:
        go = False

# Gets the user to enter the base length
go = True
while go:
    try:
        base = float(input("Enter the base length of the triangle: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        go = False

# Calculates the area of the triangle
area = (1/2 * base * height)
# Prints message displaying the area
print("\nThe area of this triangle is:", area)