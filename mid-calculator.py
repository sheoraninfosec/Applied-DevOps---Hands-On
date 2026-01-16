# Date Created: 16th January 
# Author : Jigesh Sheoran 

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b
def percentage(a, b):
    return (a * b) / 100


while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Exit")

    choice = int(input("Enter Operation: "))

    if choice == 6:
        print("Exiting calculator.")
        break

    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))

    if choice == 1:
        print(addition(a, b))
    elif choice == 2:
        print(subtraction(a, b))
    elif choice == 3:
        print(multiplication(a, b))
    elif choice == 4:
        print(division(a, b))
    elif choice == 5:
        print(percentage(a, b))
