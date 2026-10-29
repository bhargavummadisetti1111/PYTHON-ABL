products = ["Product A", "Product B", "Product C"]

production = [
    [100, 200, 150],
    [5, 30, 10]
]

threshold = 10

for i in range(len(products)):
    total = production[0][i]
    defective = production[1][i]
    percentage = defective / total * 100

    print(products[i])
    print("Production:", total)
    print("Defective units:", defective)
    print("Defect percentage:", round(percentage, 2), "%")

    if percentage > threshold:
        print("Quality threshold exceeded")
    else:
        print("Quality acceptable")