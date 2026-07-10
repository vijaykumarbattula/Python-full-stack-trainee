# Grocery Bill Calculator

items = {
    1: {"name": "Rice", "price": 60},
    2: {"name": "Sugar", "price": 45},
    3: {"name": "Milk", "price": 30},
    4: {"name": "Bread", "price": 40},
    5: {"name": "Egg", "price": 6},
    6: {"name": "Oil", "price": 150}
}

cart = []
subtotal = 0

print("=" * 40)
print("      GROCERY BILL CALCULATOR")
print("=" * 40)

while True:
    print("\nAvailable Items")
    print("-" * 40)

    for key, value in items.items():
        print(f"{key}. {value['name']} - ₹{value['price']}")

    try:
        choice = int(input("\nEnter Item Number (1-6): "))

        if choice not in items:
            print("Invalid Item Number!")
            continue

        quantity = int(input("Enter Quantity: "))

        item_name = items[choice]["name"]
        price = items[choice]["price"]
        total = price * quantity

        cart.append((item_name, quantity, price, total))
        subtotal += total

        again = input("\nAdd another item? (yes/no): ").lower()

        if again != "yes":
            break

    except ValueError:
        print("Please enter numbers only!")

# Discount
discount = 0

if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05

amount = subtotal - discount
gst = amount * 0.05
final_bill = amount + gst

print("\n")
print("=" * 45)
print("              FINAL BILL")
print("=" * 45)

print("{:<15}{:<10}{:<10}".format("Item", "Qty", "Total"))
print("-" * 45)

for item in cart:
    print("{:<15}{:<10}{:<10}".format(item[0], item[1], item[3]))

print("-" * 45)
print(f"Subtotal : ₹{subtotal:.2f}")
print(f"Discount : ₹{discount:.2f}")
print(f"GST (5%) : ₹{gst:.2f}")
print(f"Total Bill : ₹{final_bill:.2f}")
print("=" * 45)
print("     Thank You! Visit Again.")
print("=" * 45)