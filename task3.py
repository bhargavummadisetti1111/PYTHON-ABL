stock = {"Burger": 10, "Pizza": 5, "Juice": 8}
price = {"Burger": 50, "Pizza": 100, "Juice": 30}
sales = 0

orders = [
    ("Burger", 2),
    ("Pizza", 1),
    ("Juice", 3),
    ("Pizza", 6)
]

for item, qty in orders:
    if item in stock and qty > 0 and qty <= stock[item]:
        bill = price[item] * qty
        stock[item] -= qty
        sales += bill
        print(item, "Bill:", bill)
    else:
        print(item, "Order rejected")

print("Total sales:", sales)
print("Remaining stock:", stock)