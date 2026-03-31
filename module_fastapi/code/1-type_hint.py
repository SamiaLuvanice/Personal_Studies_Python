# Sem type hint
def hello(name):
    return f"Hello, {name}!"

print(hello("Alice"))

# Com type hint
def hello2(name: str) -> str:
    return f"Hello, {name}!"

print(hello2("Bob"))

# Com Lista
# Sem type hint
list_users  = [ 
    "Fulano", "Sicrano"
]

# Com type hint
list_users2: list[str] = [
    "Fulano", "Sicrano"
]

# Com Dicionário
# Sem type hint
dict_users = {
    "name": "Fulano",
    "age": 30
}

# Com type hint
dict_users2: dict[str, str] = {
    "name": "Fulano",
    "age": "30"
}

print(list_users)
print(list_users2)
print(dict_users)
print(dict_users2)