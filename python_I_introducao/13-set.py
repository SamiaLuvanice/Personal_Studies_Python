# Não possibilita recuperar valores por índice, mas é possível verificar se um item existe no conjunto
# Não possibilita recuperar valores via fatiamento ou slice

gameSet = {"Mario", "Zelda", "Sonic"}
print(gameSet)
print(type(gameSet))

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True e 1 são considerados o mesmo valor, assim como False e 0
exampleSet = {1, 2, 3, True, False, 0}
print(exampleSet)

# 3 - Adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 - Remover um item do set
gameSet.remove("Sonic")
print(gameSet)