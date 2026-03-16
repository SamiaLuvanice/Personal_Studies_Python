courses = []

with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)

print(courses)

for course in sorted(courses, key=lambda course: course["language"], reverse=True):
    print(f"{course['language']} - {course['category']}")
