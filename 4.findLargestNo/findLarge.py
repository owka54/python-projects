# Find the largetst number

# Gets the first number input
while True:
    try:
        num1 = int(input("Enter the first number: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        break

# Gets the second number input
while True:
    try:
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        break

# Checks which statement is true and prints the correct message
if num1 < num2:
    print(num2, "is larger than", num1)
elif num1 > num2:
    print(num1, "is larger than", num2)
elif num1 == num2:
    print(num1, "is equal to", num2)