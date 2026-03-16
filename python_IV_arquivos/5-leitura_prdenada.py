courses = []

with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, applicability = line.rstrip().split(",")
        courses.append((f"{language}", f"{applicability}"))

for course in sorted(courses, reverse=True):
    print(course)
