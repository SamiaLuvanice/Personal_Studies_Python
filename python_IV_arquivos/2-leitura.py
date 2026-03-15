from pathlib import Path

names_path = Path(__file__).resolve().parent.parent / "names.txt"

with open(names_path, "r", encoding="cp1252") as file:
    for line in file:
        print(f"Olá, {line.rstrip()}")
