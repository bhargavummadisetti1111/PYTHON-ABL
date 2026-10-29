books = [
    ("B101", 5, 8),
    ("B102", 7, 7),
    ("B103", 4, 10),
    ("B104", 6, 9)
]

available = 4
fine_per_day = 5
total_fine = 0

for book, allowed, returned in books:
    delay = returned - allowed

    if delay > 0:
        fine = delay * fine_per_day
        total_fine += fine
        print(book, "Overdue days:", delay, "Fine:", fine)
    else:
        print(book, "Returned on time")

    available += 1

print("Total fine:", total_fine)
print("Available books:", available)