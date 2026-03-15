names = []

with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())

names.sort()

for name in names:
    print(f"Olá, {name}")
