
foods =[]
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("\nYour shopping cart:")
for food in foods:
    print(food, end=", ")

for price in prices:
    total += price
print(f"\nTotal price: ${total}")