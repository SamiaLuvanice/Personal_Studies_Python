gamesList = ["The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey", "Animal Crossing: New Horizons", "Hades", "Celeste"]

# 1 - Iterando valores de uma lista
for game in gamesList:
    print(game)

# 2 - Quando a condição for atendida, o loop será encerrado
for game in gamesList:
  if game == "Animal Crossing: New Horizons":
    print("Jogo encontrado!")
    break
  print(game)

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for game in gamesList:
    if game == "Hades":
      print("Jogo encontrado!")
      continue
    print(game)

# 4 - Avaliação do jogo
gameName = input("Digite o nome do jogo:\n")
gameRating = int(input(f"Digite quantas avaliações deseja fazer no jogo {gameName}\n"))

sum = 0
for i in range(gameRating):
  note = float(input(f"Digite a nota do jogo {i + 1} (0 a 10)\n"))
  sum += note
print(f"A média do jogo {gameName} é: {sum / gameRating:.2f}")
