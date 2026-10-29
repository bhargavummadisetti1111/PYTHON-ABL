scores = [80, 60, 90, 70, 85, 65]
group_size = 2

scores.sort(reverse=True)
groups = [[] for i in range(len(scores) // group_size)]
totals = [0] * len(groups)

for score in scores:
    index = totals.index(min(totals))
    if len(groups[index]) < group_size:
        groups[index].append(score)
        totals[index] += score
    else:
        for i in range(len(groups)):
            if len(groups[i]) < group_size:
                groups[i].append(score)
                totals[i] += score
                break

for i in range(len(groups)):
    print("Group", i + 1, ":", groups[i])
    print("Total score:", totals[i])