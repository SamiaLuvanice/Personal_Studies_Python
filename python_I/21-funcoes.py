# 1 - Função para imprimir uma mensagem de boas-vindas
def wellcome():
    print('Bem Vindo ao Curso de Python!')

wellcome()

# 2 - Funçao para somar dois números
def sum():
    return 4 + 5
print(sum())

# 3 - Função para cadastrar um jogo
def create_game():
  name = input('Digite o nome do jogo: ')
  yearLauch = int(input('Digite o ano de lançamento do jogo: '))
  gamePricing = float(input('Digite o preço do jogo: '))
  noteRating = float(input('Digite a nota de avaliação do jogo: '))

  print(f'Nome do jogo: {name} - Ano de lançamento: {yearLauch} - Preço do jogo: R${gamePricing:.2f} - Nota de avaliação: {noteRating:.1f}')

create_game()
create_game()
