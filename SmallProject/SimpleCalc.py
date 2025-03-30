# Python Simple Arithmetic Calculator
print("Python Calculator")

#   Function to add number
def add(a, b):
    return a + b

#   Function to subtract number
def sub(a, b):
    return a - b

#   Function to multiply number
def mul(a, b):
    return a * b

#   Function to divide number
def div(a, b):
    return a / b

equal = "The number is: "
choices = ["q",r"+",r"-",r"*",r"/"]

while True:

#   Input the operator from the user
    operator = input("Please enter an operator (+ - * /) or press \"q\" to quit calculator: ")

    if operator not in choices:     # It took me 2 hours to implement this thing. Somehow fix it by putting the operator inside the while loop
        print(f"{operator} is not an operator!")
        continue

    elif operator == "q":
        break

    else:
        try:
            a = float(input("Enter the 1st number: "))
            b = float(input("Enter the 2nd number: "))

            if operator == "+":
                print(equal, add(a, b))

            elif operator == "-":
                print(equal, sub(a, b))

            elif operator == "*":
                print(equal, mul(a, b))

            elif operator == "/":
                print(equal, div(a, b))

#   Executed if user didn't input a number
        except ValueError:
            print("Invalid. Please enter a number!")

#   Executed if user try to divide by zero
        except ZeroDivisionError:
            print("You cannot divide by zero!")  
