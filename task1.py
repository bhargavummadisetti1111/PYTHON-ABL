transactions = [
    (101, 500, "Deposit"),
    (102, 200, "Withdraw"),
    (101, 300, "Deposit"),
    (103, -100, "Withdraw"),
    (104, 700, "Deposit")
]

seen = []

for tid, amount, ttype in transactions:
    if tid in seen:
        print(tid, "Duplicate transaction ID")
    else:
        seen.append(tid)

    if amount <= 0:
        print(tid, "Invalid amount")

print("Suspicious sequences:")

for i in range(1, len(transactions)):
    if transactions[i][2] == transactions[i-1][2]:
        print(transactions[i-1][0], "and", transactions[i][0])