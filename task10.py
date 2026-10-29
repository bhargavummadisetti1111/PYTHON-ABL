registrations = [
    ("S101", "Python"),
    ("S102", "Java"),
    ("S101", "Python"),
    ("S103", "Advanced Python"),
    ("S104", "Java")
]

valid_courses = ["Python", "Java", "Math"]
seen = []

for student, course in registrations:
    record = (student, course)

    if record in seen:
        print("Duplicate registration:", record)
    else:
        seen.append(record)

    if course not in valid_courses:
        print("Invalid course:", student, course)

print("Valid unique registrations:")

for student, course in seen:
    if course in valid_courses:
        print(student, course)