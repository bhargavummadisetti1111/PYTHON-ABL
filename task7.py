seats = [
    [101, 102, 0],
    [103, 104, 105],
    [101, -1, 106]
]

reserved = [-1]
roll_numbers = []
empty = 0
invalid = 0

for row in seats:
    for seat in row:
        if seat == 0:
            empty += 1
        elif seat == -1:
            print("Reserved seat")
        elif seat < -1:
            invalid += 1
            print("Invalid allocation:", seat)
        elif seat in roll_numbers:
            invalid += 1
            print("Duplicate roll number:", seat)
        else:
            roll_numbers.append(seat)

print("Empty seats:", empty)
print("Invalid allocations:", invalid)
print("Valid students:", len(roll_numbers))