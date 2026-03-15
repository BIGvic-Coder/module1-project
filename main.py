# Module 1 Project
# This program demonstrates a simple calculator

def add(a, b):
    # This function adds two numbers
    return a + b

def subtract(a, b):
    # This function subtracts two numbers
    return a - b

def main():
    print("Calculator Program")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Sum:", add(num1, num2))
    print("Difference:", subtract(num1, num2))

main()