# Concession stand program

menu = {
    "soda": 2.00,
    "pop corn": 3.50,
    "hot dog": 2.00,
    "hamburger": 5.00,
    "water": 1.00,
    "pizza": 3.50
    }

cart = []
total = 0

print("----------Menu----------")

for key, value in menu.items():
    print(f"{key:10}: ${value}")

print("------------------------")

while True:
    food = input("Select menu (q to quit): ").lower()
    
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()

print(f"Total is: ${total:.2f}")    