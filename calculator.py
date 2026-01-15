# Date Created : 15th January 2026
# Author: Jigesh Sheoran

def addition (a, b):
    return a + b
def subtraction (a, b):
    return a - b
def multiplication (a, b):
    return a * b
def division (a, b):
    return a / b  

while True:
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter Operation: "))

    if choice == 5:
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
    