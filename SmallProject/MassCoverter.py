def KtL(mass):
    return (mass * 2.205)

def LtK(mass):
    return (mass / 2.205)

while True:
    print("K = Pound => Kilogram")
    print("L = Kilogram => Pound")
    print("Q = Quit")

    weight = str(input("Select your weight measurement(K or L): ")).upper()
    mass = float(input("Enter your weight number: "))

    if weight == "Q":
        break

    elif weight == "K":
        print(LtK(mass), "Kg")

    elif weight == "L":
        print(KtL(mass), "Lbs")

    else:
        print(f"{weight} is not valid")