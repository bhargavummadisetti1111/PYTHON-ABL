routes = [("Route A", 120), ("Route B", 85), ("Route C", 200)]
capacity = 50
total_buses = 0
total_unserved = 0

for route, passengers in routes:
    buses = passengers // capacity

    if passengers % capacity != 0:
        buses += 1

    served = buses * capacity
    unserved = max(0, passengers - served)

    total_buses += buses
    total_unserved += unserved

    print(route, "Buses needed:", buses)
    print("Unserved passengers:", unserved)

print("Total buses:", total_buses)
print("Total unserved:", total_unserved)