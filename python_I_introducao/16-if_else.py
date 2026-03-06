name = input("Digite o nome do jogo\n")
year = int(input("Digite o ano de lançamento do jogo\n"))
classification = float(input("Digite a classificação do jogo\n"))

if classification > 8.0 and year > 2015:
    print(f"O jogo {name} é um ótimo jogo, recomendo jogar!")
else:
    print(f"O jogo {name} é um jogo ruim, não recomendo jogar.")
