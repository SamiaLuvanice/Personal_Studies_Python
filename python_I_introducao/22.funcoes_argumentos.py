# 1 - Cire uma função que receba dois argumentos : o primeiro nome e o segundo nome
def full_name(fname, lname):
  print(f'Nome completo: {fname} {lname}')

full_name('Luan', 'Silva')

# 2 - Crie uma função que some dois números via parametros
def sum(a, b):
  return a + b

print(sum(5, 10))

# 3 - Argunmentos default numa função
def address(country='Brasil'):
  print(f'Eu moro no {country}')

address()
address('México')

# 4  - Avaliação do jogo
def rating_game(qtdRating):
  game_name = input ('Qual o nome do jogo? ')
  sum = 0
  for i in range(qtdRating):
    note = float(input(f'Digite a nota para o jogo {game_name}? '))
    sum += note
  print(f'A média das notas do jogo {game_name} é: {sum/qtdRating}')

rating = int(input('Quantas notas para avaliar o jogo? '))
rating_game(rating)
