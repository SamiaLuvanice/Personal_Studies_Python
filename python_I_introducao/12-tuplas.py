
# Não possibilita adicionar e remover itens, mas é possível acessar os itens pelo índice
# Não é possível ordenar uma tupla, mas é possível ordenar uma lista e depois converter para tupla

gamesTuple = ("The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey",
               "Hollow Knight", "Celeste", "Stardew Valley")
print(gamesTuple)
print(type(gamesTuple))

# 1 - Buscar os 2 primeiros itens da tupla
print(gamesTuple[0:2])

# 2 - Buscra o último item da tupla
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo índice
print(gamesTuple.index("Celeste"))  # Retorna o índice do item "Cel