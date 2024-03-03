#Addition
def add(no.1, no.2):
    return no.1 + no.2

#Subtraction
def subtract(no.1, no.2):
    return no.1 - no.2

#Multiplication
def multiply(no.1, no.2):
    return no.1 * no.2

#Division
def divide(no.1, no.2):
    if no.2 == 0:
        return "Error! Division by zero."
    else:
        return no.1 / no.2

#CALCULATOR

def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter operation choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation choice.")

if __name__ == "__main__":
    calculator()
