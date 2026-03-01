gameName = input("Digite o nome do jogo:\n")
qtdRatings = 0
totalRatings = 0
rating = 0
average = 0

while(rating != -1):
  rating = float(input(f"Digite a nota do jogo {gameName} (0 a 10) ou -1 para sair\n"))
  if rating != -1:
    totalRatings += rating
    qtdRatings += 1
    average = totalRatings / qtdRatings
print(f"A média do jogo {gameName} é: {average:.2f}")
