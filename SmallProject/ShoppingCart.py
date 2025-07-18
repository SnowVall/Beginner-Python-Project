# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = str(input("Enter a food to buy (q to quit): ").lower())
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print()
print("------Your Cart------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")