

menu = {"popcorn": 5.00,
        "candy": 2.00, 
        "drink": 3.00,
        "nachos": 4.00,
        "hot dog": 3.50,
        "pretzel": 3.00}
cart = []
total = 0   
print("-----------MENU------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------")

while True:
    food = input("Enter a food to buy (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------------------")
for food in cart:
    total += menu.get(food)
    print(food,end =" ")

print(f"\nTotal price: ${total:.2f}")