with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, applicability = line.rstrip().split(",")
        print(f"Curso: {language}, Aplicabilidade: {applicability}")
