import random

while True:
    roll = str(input("Role the dice? (Y/n): ")).upper()

    if roll == "Y":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print(f"({a}, {b})")

    elif roll == "N":
        break

    else:
        print("Invalid choices!")