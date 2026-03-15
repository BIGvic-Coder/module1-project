# Module 1 Project
# Author: Victor
# Description: This program is a command-line calculator that performs
# addition, subtraction, multiplication, and division.
# It allows users to repeatedly perform calculations until they choose to exit.

# -------------------------------------------------------
# Function: add
# Description: Adds two numbers and returns the result
# -------------------------------------------------------
def add(a, b):
    return a + b


# -------------------------------------------------------
# Function: subtract
# Description: Subtracts the second number from the first
# -------------------------------------------------------
def subtract(a, b):
    return a - b


# -------------------------------------------------------
# Function: multiply
# Description: Multiplies two numbers
# -------------------------------------------------------
def multiply(a, b):
    return a * b


# -------------------------------------------------------
# Function: divide
# Description: Divides the first number by the second
# Includes error handling for division by zero
# -------------------------------------------------------
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b


# -------------------------------------------------------
# Function: display_menu
# Description: Shows the calculator options
# -------------------------------------------------------
def display_menu():
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


# -------------------------------------------------------
# Function: get_numbers
# Description: Gets two numbers from the user
# -------------------------------------------------------
def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2


# -------------------------------------------------------
# Function: main
# Description: Controls the program flow
# -------------------------------------------------------
def main():

    print("Welcome to the Python Calculator Program")

    # Loop so the calculator continues running
    while True:

        # Display calculator options
        display_menu()

        # Ask the user for their choice
        choice = input("Choose an operation (1-5): ")

        # Perform addition
        if choice == "1":
            num1, num2 = get_numbers()
            result = add(num1, num2)
            print("Result:", result)

        # Perform subtraction
        elif choice == "2":
            num1, num2 = get_numbers()
            result = subtract(num1, num2)
            print("Result:", result)

        # Perform multiplication
        elif choice == "3":
            num1, num2 = get_numbers()
            result = multiply(num1, num2)
            print("Result:", result)

        # Perform division
        elif choice == "4":
            num1, num2 = get_numbers()
            result = divide(num1, num2)
            if result is not None:
                print("Result:", result)

        # Exit program
        elif choice == "5":
            print("Thank you for using the calculator.")
            break

        # Handle invalid choices
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


# Run the program
main()