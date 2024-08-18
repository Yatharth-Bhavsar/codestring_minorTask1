import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    return math.sqrt(x)

def calculator():
    while True:
        print("\nSimple Calculator Menu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")
        
        choice = input("Select an operation (1-7): ")
        
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
        
        elif choice == '6':
            num = float(input("Enter a number: "))
            print(f"Result: √{num} = {square_root(num)}")
        
        else:
            print("Invalid choice. Please select a valid option.")

calculator()
