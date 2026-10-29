products = ["Pen", "Book", "Bag"]

prices = [
    [10, 50, 500],
    [12, 45, 600],
    [15, 60, 550]
]

threshold = 20
fluctuations = []

for i in range(len(products)):
    old_price = prices[0][i]
    new_price = prices[-1][i]

    change = (new_price - old_price) / old_price * 100
    fluctuations.append(abs(change))

    print(products[i])
    print("Price change:", round(change, 2), "%")

    if abs(change) > threshold:
        print("Threshold exceeded")
    else:
        print("Within threshold")

index = fluctuations.index(max(fluctuations))
print("Maximum fluctuation:", products[index])