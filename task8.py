areas = ["Area A", "Area B", "Area C"]

demand = [
    [100, 120, 110],
    [150, 130, 140],
    [90, 100, 95]
]

supply = [
    [90, 100, 100],
    [120, 100, 120],
    [90, 90, 80]
]

shortages = []

for i in range(len(areas)):
    total_demand = sum(demand[i])
    total_supply = sum(supply[i])
    shortage = total_demand - total_supply

    if shortage < 0:
        shortage = 0

    shortages.append(shortage)

    print(areas[i])
    print("Demand:", total_demand)
    print("Supply:", total_supply)
    print("Shortage:", shortage)

index = shortages.index(max(shortages))
print("Most underserved area:", areas[index])