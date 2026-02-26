gamesList = ["Fifa23", "GTA5", "Minecraft", "Valorant", "Fortnite",
              "Call of Duty", "Apex Legends", "League of Legends", 
              "Overwatch", "Cyberpunk 2077"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recuperar um item da lista pelo indice
print(gamesList.index("Valorant"))  # Retorna o índice do item "Valorant"

# 3 - Adicionar item ao final da lista
gamesList.append("Among Us")
print(gamesList)

# 4 - Ordenar lista
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra
newGamesList = gamesList.copy() 
newGamesList.remove("Cyberpunk 2077")  # Removendo um item da nova lista para mostrar que são independentes
print(newGamesList)

# 6 - Limpar a lista
newGamesList.clear()
